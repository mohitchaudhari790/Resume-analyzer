from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Q
from .models import Profile, Resume, Job, Application, SavedJob, ResumeAnalysis, ExtractedSkill
from .forms import UserRegisterForm, ProfileForm, ResumeUploadForm, JobForm, AdvancedJobSearchForm
from .ai_utils import parse_resume, analyze_resume as ai_analyze_resume, calculate_job_match, get_job_recommendations, get_missing_skills_for_job
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
import os

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'portal/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'portal/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    profile = Profile.objects.get_or_create(user=request.user)[0]
    resumes = Resume.objects.filter(user=request.user).order_by('-uploaded_at')[:5]
    applications = Application.objects.filter(user=request.user).order_by('-applied_at')[:5]
    saved_jobs = SavedJob.objects.filter(user=request.user).count()
    total_jobs = Job.objects.filter(is_active=True).count()
    total_resumes = Resume.objects.filter(user=request.user).count()
    
    context = {
        'profile': profile,
        'resumes': resumes,
        'applications': applications,
        'saved_jobs_count': saved_jobs,
        'total_jobs': total_jobs,
        'total_resumes': total_resumes,
    }
    return render(request, 'portal/dashboard.html', context)

@login_required
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            
            parsed_data = parse_resume(resume.file.path)
            resume.parsed_text = parsed_data['text']
            resume.save()
            
            for skill in parsed_data['skills']:
                ExtractedSkill.objects.create(resume=resume, skill_name=skill)
            
            messages.success(request, 'Resume uploaded successfully!')
            return redirect('analyze_resume', resume_id=resume.id)
    else:
        form = ResumeUploadForm()
    return render(request, 'portal/upload_resume.html', {'form': form})

@login_required
def analyze_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    
    analysis, created = ResumeAnalysis.objects.get_or_create(resume=resume)
    if created or not analysis.detected_skills:
        analysis_data = ai_analyze_resume(resume)
        analysis.detected_skills = ', '.join(analysis_data['detected_skills'])
        analysis.missing_skills = ', '.join(analysis_data['missing_skills'])
        analysis.grammar_suggestions = '\n'.join(analysis_data['grammar_suggestions'])
        analysis.keyword_suggestions = ', '.join(analysis_data['keyword_suggestions'])
        resume.ats_score = analysis_data['ats_score']
        resume.save()
        analysis.save()
    
    # Get all active jobs for recommendations
    all_jobs = Job.objects.filter(is_active=True)
    job_recommendations = get_job_recommendations(resume, all_jobs)
    
    # Get top 10 recommendations
    top_recommendations = job_recommendations[:10]
    
    context = {
        'resume': resume,
        'analysis': analysis,
        'job_recommendations': top_recommendations,
        'total_jobs_analyzed': len(all_jobs),
    }
    return render(request, 'portal/analyze_resume.html', context)

@login_required
def job_listings(request):
    """Advanced job listings with search and filters"""
    form = AdvancedJobSearchForm(request.GET)
    jobs = Job.objects.filter(is_active=True).order_by('-posted_at')
    
    # Get user's resume skills for match calculation
    user_skills = []
    if Resume.objects.filter(user=request.user).exists():
        latest_resume = Resume.objects.filter(user=request.user).latest('uploaded_at')
        user_skills = [skill.skill_name.lower() for skill in latest_resume.extracted_skills.all()]
    
    if form.is_valid():
        # Search query (title, company, skills)
        query = form.cleaned_data.get('query')
        if query:
            jobs = jobs.filter(
                Q(title__icontains=query) | 
                Q(company__icontains=query) | 
                Q(required_skills__icontains=query) |
                Q(description__icontains=query)
            )
        
        # Location filter
        location = form.cleaned_data.get('location')
        if location:
            jobs = jobs.filter(location__icontains=location)
        
        # Job type filter
        job_types = form.cleaned_data.get('job_type')
        if job_types:
            jobs = jobs.filter(job_type__in=job_types)
        
        # Experience level filter
        experience_levels = form.cleaned_data.get('experience_level')
        if experience_levels:
            jobs = jobs.filter(experience_level__in=experience_levels)
        
        # Salary range filter
        salary_min = form.cleaned_data.get('salary_min')
        salary_max = form.cleaned_data.get('salary_max')
        if salary_min:
            jobs = jobs.filter(salary_max__gte=salary_min)
        if salary_max:
            jobs = jobs.filter(salary_min__lte=salary_max)
        
        # Skills filter
        skills_query = form.cleaned_data.get('skills')
        if skills_query:
            skills_list = [s.strip() for s in skills_query.split(',')]
            for skill in skills_list:
                jobs = jobs.filter(required_skills__icontains=skill)
    
    # Calculate match scores for each job
    jobs_with_match = []
    for job in jobs:
        match_score = 0
        matched_skills = []
        missing_skills = []
        
        if user_skills:
            job_skills = [s.strip().lower() for s in job.required_skills.split(',')]
            matched_skills = [s for s in user_skills if s in job_skills]
            missing_skills = [s for s in job_skills if s not in user_skills]
            
            if job_skills:
                match_score = int((len(matched_skills) / len(job_skills)) * 100)
        
        # Check if job is saved
        is_saved = SavedJob.objects.filter(user=request.user, job=job).exists()
        has_applied = Application.objects.filter(user=request.user, job=job).exists()
        
        jobs_with_match.append({
            'job': job,
            'match_score': match_score,
            'matched_skills': matched_skills[:5],  # Show top 5
            'missing_skills': missing_skills[:5],  # Show top 5
            'is_saved': is_saved,
            'has_applied': has_applied,
        })
    
    # Sort by match score if user has resume
    if user_skills:
        jobs_with_match.sort(key=lambda x: x['match_score'], reverse=True)
    
    context = {
        'jobs_with_match': jobs_with_match,
        'form': form,
        'total_jobs': len(jobs_with_match),
        'has_resume': bool(user_skills),
    }
    return render(request, 'portal/job_listings.html', context)

@login_required
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    is_saved = SavedJob.objects.filter(user=request.user, job=job).exists()
    has_applied = Application.objects.filter(user=request.user, job=job).exists()
    
    match_score = 0
    matched_skills = []
    missing_skills = []
    
    if Resume.objects.filter(user=request.user).exists():
        latest_resume = Resume.objects.filter(user=request.user).latest('uploaded_at')
        match_score = calculate_job_match(latest_resume, job)
        missing_skills = get_missing_skills_for_job(latest_resume, job)
        
        # Get matched skills
        resume_text = latest_resume.parsed_text.lower()
        from .ai_utils import COMMON_SKILLS
        resume_skills = set([skill for skill in COMMON_SKILLS if skill in resume_text])
        job_required_skills = set([skill.strip().lower() for skill in job.required_skills.split(',')])
        matched_skills = list(resume_skills.intersection(job_required_skills))
    
    context = {
        'job': job,
        'is_saved': is_saved,
        'has_applied': has_applied,
        'match_score': match_score,
        'matched_skills': matched_skills,
        'missing_skills': missing_skills,
    }
    return render(request, 'portal/job_detail.html', context)

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if not Resume.objects.filter(user=request.user).exists():
        messages.error(request, 'Please upload a resume first!')
        return redirect('upload_resume')
    
    latest_resume = Resume.objects.filter(user=request.user).latest('uploaded_at')
    match_score = calculate_job_match(latest_resume, job)
    
    application, created = Application.objects.get_or_create(
        user=request.user,
        job=job,
        defaults={'resume': latest_resume, 'match_score': match_score}
    )
    
    if created:
        messages.success(request, f'Successfully applied to {job.title}!')
    else:
        messages.info(request, 'You have already applied to this job.')
    
    return redirect('job_detail', job_id=job_id)

@login_required
def ai_job_match(request):
    if not Resume.objects.filter(user=request.user).exists():
        messages.warning(request, 'Please upload a resume first to see job matches.')
        return redirect('upload_resume')
    
    latest_resume = Resume.objects.filter(user=request.user).latest('uploaded_at')
    jobs = Job.objects.filter(is_active=True)
    
    job_matches = []
    for job in jobs:
        match_score = calculate_job_match(latest_resume, job)
        if match_score > 30:
            job_matches.append({'job': job, 'match_score': match_score})
    
    job_matches.sort(key=lambda x: x['match_score'], reverse=True)
    
    context = {'job_matches': job_matches[:10], 'resume': latest_resume}
    return render(request, 'portal/ai_job_match.html', context)

@login_required
def saved_jobs(request):
    saved = SavedJob.objects.filter(user=request.user).select_related('job')
    context = {'saved_jobs': saved}
    return render(request, 'portal/saved_jobs.html', context)

@login_required
def save_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    SavedJob.objects.get_or_create(user=request.user, job=job)
    messages.success(request, 'Job saved successfully!')
    return redirect('job_detail', job_id=job_id)

@login_required
def unsave_job(request, job_id):
    SavedJob.objects.filter(user=request.user, job_id=job_id).delete()
    messages.success(request, 'Job removed from saved list.')
    return redirect('saved_jobs')

@login_required
def application_tracker(request):
    applications = Application.objects.filter(user=request.user).select_related('job').order_by('-applied_at')
    
    status_filter = request.GET.get('status', '')
    if status_filter:
        applications = applications.filter(status=status_filter)
    
    context = {'applications': applications, 'status_filter': status_filter}
    return render(request, 'portal/application_tracker.html', context)

@login_required
def profile_settings(request):
    profile = Profile.objects.get_or_create(user=request.user)[0]
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            request.user.first_name = request.POST.get('first_name', '')
            request.user.last_name = request.POST.get('last_name', '')
            request.user.email = request.POST.get('email', '')
            request.user.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile_settings')
    else:
        form = ProfileForm(instance=profile)
    
    context = {'form': form, 'profile': profile}
    return render(request, 'portal/profile_settings.html', context)

@staff_member_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('job_listings')
    else:
        form = JobForm()
    return render(request, 'portal/add_job.html', {'form': form})

@login_required
def recommended_jobs(request):
    """Show AI-recommended jobs based on user's resume"""
    if not Resume.objects.filter(user=request.user).exists():
        messages.warning(request, 'Please upload a resume to get personalized job recommendations.')
        return redirect('upload_resume')
    
    latest_resume = Resume.objects.filter(user=request.user).latest('uploaded_at')
    user_skills = [skill.skill_name.lower() for skill in latest_resume.extracted_skills.all()]
    
    if not user_skills:
        messages.warning(request, 'No skills detected in your resume. Please upload a better resume.')
        return redirect('upload_resume')
    
    # Get all active jobs
    all_jobs = Job.objects.filter(is_active=True)
    
    # Calculate match scores
    recommendations = []
    for job in all_jobs:
        job_skills = [s.strip().lower() for s in job.required_skills.split(',')]
        matched_skills = [s for s in user_skills if s in job_skills]
        missing_skills = [s for s in job_skills if s not in user_skills]
        
        if job_skills:
            match_score = int((len(matched_skills) / len(job_skills)) * 100)
        else:
            match_score = 0
        
        # Only recommend jobs with at least 30% match
        if match_score >= 30:
            is_saved = SavedJob.objects.filter(user=request.user, job=job).exists()
            has_applied = Application.objects.filter(user=request.user, job=job).exists()
            
            recommendations.append({
                'job': job,
                'match_score': match_score,
                'matched_skills': matched_skills,
                'missing_skills': missing_skills,
                'is_saved': is_saved,
                'has_applied': has_applied,
            })
    
    # Sort by match score
    recommendations.sort(key=lambda x: x['match_score'], reverse=True)
    
    context = {
        'recommendations': recommendations[:20],  # Top 20 recommendations
        'total_recommendations': len(recommendations),
    }
    return render(request, 'portal/recommended_jobs.html', context)

@login_required
def saved_resumes(request):
    resumes = Resume.objects.filter(user=request.user).prefetch_related('extracted_skills').order_by('-uploaded_at')
    context = {'resumes': resumes}
    return render(request, 'portal/saved_resumes.html', context)

@login_required
def delete_resume(request, resume_id):
    if request.method == 'POST':
        resume = get_object_or_404(Resume, id=resume_id, user=request.user)
        
        # Delete the file from storage
        if resume.file:
            if os.path.isfile(resume.file.path):
                os.remove(resume.file.path)
        
        # Delete the resume record
        resume.delete()
        
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

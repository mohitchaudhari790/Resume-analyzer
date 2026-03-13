from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=100, blank=True)
    skills = models.TextField(blank=True)
    education = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    linkedin = models.URLField(blank=True)
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    parsed_text = models.TextField(blank=True)
    ats_score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    def __str__(self):
        return f"{self.user.username} - {self.uploaded_at.strftime('%Y-%m-%d')}"

class ExtractedSkill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='extracted_skills')
    skill_name = models.CharField(max_length=100)
    confidence = models.FloatField(default=1.0)
    
    def __str__(self):
        return self.skill_name

class Job(models.Model):
    EXPERIENCE_CHOICES = [
        ('entry', 'Entry Level (0-2 years)'),
        ('mid', 'Mid Level (2-5 years)'),
        ('senior', 'Senior Level (5+ years)'),
    ]
    
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('internship', 'Internship'),
        ('contract', 'Contract'),
        ('remote', 'Remote'),
    ]
    
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    company_website = models.URLField(blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='full_time')
    salary_min = models.IntegerField(blank=True, null=True)
    salary_max = models.IntegerField(blank=True, null=True)
    required_skills = models.TextField()
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='entry')
    description = models.TextField()
    deadline = models.DateField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title} at {self.company}"
    
    def get_posted_time(self):
        """Return human-readable posted time"""
        from django.utils import timezone
        from datetime import timedelta
        
        now = timezone.now()
        diff = now - self.posted_at
        
        if diff < timedelta(hours=1):
            return "Posted just now"
        elif diff < timedelta(days=1):
            hours = int(diff.total_seconds() / 3600)
            return f"Posted {hours} hour{'s' if hours > 1 else ''} ago"
        elif diff < timedelta(days=7):
            days = diff.days
            return f"Posted {days} day{'s' if days > 1 else ''} ago"
        elif diff < timedelta(days=30):
            weeks = diff.days // 7
            return f"Posted {weeks} week{'s' if weeks > 1 else ''} ago"
        else:
            months = diff.days // 30
            return f"Posted {months} month{'s' if months > 1 else ''} ago"

class Application(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('review', 'Under Review'),
        ('interview', 'Interview'),
        ('selected', 'Selected'),
        ('rejected', 'Rejected'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    applied_at = models.DateTimeField(auto_now_add=True)
    match_score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    class Meta:
        unique_together = ['user', 'job']
    
    def __str__(self):
        return f"{self.user.username} - {self.job.title}"

class SavedJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'job']
    
    def __str__(self):
        return f"{self.user.username} saved {self.job.title}"

class ResumeAnalysis(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE)
    detected_skills = models.TextField(blank=True)
    missing_skills = models.TextField(blank=True)
    grammar_suggestions = models.TextField(blank=True)
    keyword_suggestions = models.TextField(blank=True)
    analyzed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Analysis for {self.resume.user.username}"

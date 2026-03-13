from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Resume, Job

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'city', 'skills', 'education', 'experience', 'linkedin', 'portfolio', 'profile_pic']
        widgets = {
            'skills': forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g., Python, Django, JavaScript'}),
            'education': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Your educational background'}),
            'experience': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Your work experience'}),
        }

class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={'accept': '.pdf,.docx'})
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'company_website', 'company_description', 'industry',
                  'location', 'job_type', 'salary_min', 'salary_max', 
                  'required_skills', 'experience_level', 'description', 'deadline']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'company_description': forms.Textarea(attrs={'rows': 3}),
            'required_skills': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Comma-separated skills'}),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

class AdvancedJobSearchForm(forms.Form):
    """Advanced job search and filter form"""
    query = forms.CharField(
        max_length=200, 
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by job title, company, or skills...',
            'class': 'search-input'
        })
    )
    
    location = forms.CharField(
        max_length=100, 
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Location',
            'class': 'filter-input'
        })
    )
    
    job_type = forms.MultipleChoiceField(
        choices=Job.JOB_TYPE_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'filter-checkbox'})
    )
    
    experience_level = forms.MultipleChoiceField(
        choices=Job.EXPERIENCE_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'filter-checkbox'})
    )
    
    salary_min = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Min Salary',
            'class': 'filter-input'
        })
    )
    
    salary_max = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Max Salary',
            'class': 'filter-input'
        })
    )
    
    skills = forms.CharField(
        max_length=500,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Filter by skills (comma-separated)',
            'class': 'filter-input'
        })
    )

from django.contrib import admin
from .models import Profile, Resume, ExtractedSkill, Job, Application, SavedJob, ResumeAnalysis

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'phone', 'created_at']
    search_fields = ['user__username', 'city']

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['user', 'uploaded_at', 'ats_score']
    list_filter = ['uploaded_at']
    search_fields = ['user__username']

@admin.register(ExtractedSkill)
class ExtractedSkillAdmin(admin.ModelAdmin):
    list_display = ['skill_name', 'resume', 'confidence']
    search_fields = ['skill_name']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'experience_level', 'posted_at', 'is_active']
    list_filter = ['experience_level', 'is_active', 'posted_at']
    search_fields = ['title', 'company', 'location']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'job', 'status', 'match_score', 'applied_at']
    list_filter = ['status', 'applied_at']
    search_fields = ['user__username', 'job__title']

@admin.register(SavedJob)
class SavedJobAdmin(admin.ModelAdmin):
    list_display = ['user', 'job', 'saved_at']
    search_fields = ['user__username', 'job__title']

@admin.register(ResumeAnalysis)
class ResumeAnalysisAdmin(admin.ModelAdmin):
    list_display = ['resume', 'analyzed_at']
    search_fields = ['resume__user__username']

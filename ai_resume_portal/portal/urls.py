from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    path('upload-resume/', views.upload_resume, name='upload_resume'),
    path('analyze-resume/<int:resume_id>/', views.analyze_resume, name='analyze_resume'),
    path('saved-resumes/', views.saved_resumes, name='saved_resumes'),
    path('delete-resume/<int:resume_id>/', views.delete_resume, name='delete_resume'),
    
    path('jobs/', views.job_listings, name='job_listings'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('jobs/<int:job_id>/apply/', views.apply_job, name='apply_job'),
    path('jobs/<int:job_id>/save/', views.save_job, name='save_job'),
    path('jobs/<int:job_id>/unsave/', views.unsave_job, name='unsave_job'),
    path('add-job/', views.add_job, name='add_job'),
    path('recommended-jobs/', views.recommended_jobs, name='recommended_jobs'),
    
    path('ai-job-match/', views.ai_job_match, name='ai_job_match'),
    path('saved-jobs/', views.saved_jobs, name='saved_jobs'),
    path('application-tracker/', views.application_tracker, name='application_tracker'),
    path('profile-settings/', views.profile_settings, name='profile_settings'),
]

# AI Resume Portal - Quick Reference Guide

## 🚀 Quick Start

### Option 1: Automated Setup (Windows)
```bash
cd "d:\mini project\ai_resume_portal"
setup.bat
```

### Option 2: Manual Setup
```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download spaCy model
python -m spacy download en_core_web_sm

# 5. Setup database (PostgreSQL)
# Create database: ai_resume_db
# Update credentials in config/settings.py

# 6. Run migrations
python manage.py makemigrations
python manage.py migrate

# 7. Create admin user
python manage.py createsuperuser

# 8. Populate sample data
python manage.py populate_jobs

# 9. Run server
python manage.py runserver
```

## 📁 Complete Project Structure

```
ai_resume_portal/
│
├── config/                          # Project Configuration
│   ├── __init__.py
│   ├── settings.py                 # Django settings
│   ├── urls.py                     # Main URL routing
│   ├── asgi.py                     # ASGI config
│   └── wsgi.py                     # WSGI config
│
├── portal/                          # Main Application
│   ├── management/                 # Custom commands
│   │   ├── __init__.py
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── populate_jobs.py   # Sample data generator
│   │
│   ├── migrations/                 # Database migrations
│   │   └── __init__.py
│   │
│   ├── __init__.py
│   ├── admin.py                    # Admin panel config
│   ├── ai_utils.py                 # AI/NLP utilities
│   ├── apps.py                     # App configuration
│   ├── forms.py                    # Django forms
│   ├── models.py                   # Database models
│   ├── tests.py                    # Unit tests
│   ├── urls.py                     # App URL patterns
│   └── views.py                    # View functions
│
├── templates/                       # HTML Templates
│   ├── portal/
│   │   ├── base.html              # Base template with sidebar
│   │   ├── dashboard.html         # Main dashboard
│   │   ├── login.html             # Login page
│   │   ├── register.html          # Registration page
│   │   ├── upload_resume.html     # Resume upload
│   │   ├── analyze_resume.html    # AI analysis results
│   │   ├── job_listings.html      # Job search/browse
│   │   ├── job_detail.html        # Job details
│   │   ├── ai_job_match.html      # AI recommendations
│   │   ├── saved_jobs.html        # Bookmarked jobs
│   │   ├── application_tracker.html  # Application status
│   │   ├── profile_settings.html  # User profile
│   │   ├── add_job.html           # Post job (admin)
│   │   ├── password_reset_form.html
│   │   ├── password_reset_done.html
│   │   ├── password_reset_confirm.html
│   │   └── password_reset_complete.html
│   │
│   └── registration/               # Auth templates
│       ├── password_reset_email.html
│       └── password_reset_subject.txt
│
├── static/                          # Static Files
│   ├── css/
│   │   └── style.css              # Main stylesheet (3D, animations)
│   ├── js/
│   │   └── script.js              # JavaScript functionality
│   └── images/                     # Image assets
│
├── media/                           # User Uploads
│   ├── resumes/                    # Resume files
│   └── profiles/                   # Profile pictures
│
├── manage.py                        # Django management script
├── requirements.txt                 # Python dependencies
├── README.md                        # Main documentation
├── FEATURES.md                      # Detailed features guide
├── .gitignore                       # Git ignore rules
├── .env.example                     # Environment variables template
├── database_setup.sql               # PostgreSQL setup script
├── setup.bat                        # Windows setup script
└── run.bat                          # Windows run script
```

## 🔑 Key URLs

| Page | URL | Description |
|------|-----|-------------|
| Login | `/login/` | User login |
| Register | `/register/` | New user registration |
| Dashboard | `/` | Main dashboard |
| Upload Resume | `/upload-resume/` | Upload PDF/DOCX |
| Resume Analysis | `/analyze-resume/<id>/` | AI analysis results |
| Job Listings | `/jobs/` | Browse all jobs |
| Job Detail | `/jobs/<id>/` | View job details |
| AI Job Match | `/ai-job-match/` | AI recommendations |
| Saved Jobs | `/saved-jobs/` | Bookmarked jobs |
| Applications | `/application-tracker/` | Track applications |
| Profile | `/profile-settings/` | Edit profile |
| Add Job | `/add-job/` | Post job (admin) |
| Admin Panel | `/admin/` | Django admin |
| Password Reset | `/password-reset/` | Reset password |

## 📊 Database Models

### User (Django built-in)
- username, email, password, first_name, last_name

### Profile
- user (FK), phone, city, skills, education, experience
- linkedin, portfolio, profile_pic, created_at

### Resume
- user (FK), file, uploaded_at, parsed_text, ats_score

### ExtractedSkill
- resume (FK), skill_name, confidence

### Job
- title, company, location, salary_min, salary_max
- required_skills, experience_level, description
- deadline, posted_by (FK), posted_at, is_active

### Application
- user (FK), job (FK), resume (FK)
- status, applied_at, match_score

### SavedJob
- user (FK), job (FK), saved_at

### ResumeAnalysis
- resume (FK), detected_skills, missing_skills
- grammar_suggestions, keyword_suggestions, analyzed_at

## 🎨 CSS Classes Reference

### Layout
- `.sidebar` - Left navigation
- `.main-content` - Main content area
- `.topbar` - Top navigation bar
- `.content-area` - Content wrapper

### Cards
- `.card` - Basic card
- `.stat-card` - Dashboard stat card
- `.job-card` - Job listing card
- `.application-card` - Application card

### Buttons
- `.btn` - Base button
- `.btn-primary` - Primary action
- `.btn-secondary` - Secondary action
- `.btn-success` - Success state
- `.btn-danger` - Danger/delete
- `.btn-small` - Small button
- `.btn-block` - Full width

### Forms
- `.form-control` - Input field
- `.form-group` - Form field wrapper
- `.form-row` - Two-column layout

### Status
- `.status-applied` - Applied status
- `.status-review` - Under review
- `.status-interview` - Interview
- `.status-selected` - Selected
- `.status-rejected` - Rejected

### Scores
- `.score-circle` - Circular score display
- `.progress-bar` - Progress bar
- `.match-score-badge` - Match percentage

## 🔧 Common Commands

### Development
```bash
# Run server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run shell
python manage.py shell
```

### Database
```bash
# Reset database
python manage.py flush

# Load sample data
python manage.py populate_jobs

# Backup database
pg_dump ai_resume_db > backup.sql

# Restore database
psql ai_resume_db < backup.sql
```

### Testing
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test portal

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## 🐛 Common Issues & Solutions

### Issue: Module not found
**Solution**: Activate virtual environment and install requirements
```bash
venv\Scripts\activate
pip install -r requirements.txt
```

### Issue: Database connection error
**Solution**: Check PostgreSQL is running and credentials are correct
```bash
# Check PostgreSQL status
pg_ctl status

# Update config/settings.py with correct credentials
```

### Issue: Static files not loading
**Solution**: Collect static files
```bash
python manage.py collectstatic --noinput
```

### Issue: Resume upload fails
**Solution**: Ensure media directory exists and has write permissions
```bash
mkdir media\resumes
```

### Issue: spaCy model not found
**Solution**: Download the language model
```bash
python -m spacy download en_core_web_sm
```

## 📝 Environment Variables

Create `.env` file (copy from `.env.example`):
```
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=ai_resume_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

## 🔐 Default Credentials

After running `populate_jobs` command:
- **Username**: admin
- **Password**: admin123

Change these in production!

## 📱 Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 🎯 Performance Tips

1. **Database**: Add indexes to frequently queried fields
2. **Static Files**: Use CDN in production
3. **Caching**: Implement Redis for session storage
4. **Images**: Compress profile pictures
5. **Queries**: Use select_related() and prefetch_related()

## 🚀 Deployment Checklist

- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up production database
- [ ] Configure static files serving
- [ ] Set up HTTPS/SSL
- [ ] Configure email backend
- [ ] Set strong SECRET_KEY
- [ ] Enable database backups
- [ ] Set up monitoring
- [ ] Configure logging

## 📞 Support

For issues:
1. Check README.md
2. Check FEATURES.md
3. Review Django documentation
4. Check PostgreSQL logs
5. Review browser console for errors

## 🎓 Learning Resources

- Django Docs: https://docs.djangoproject.com/
- PostgreSQL Docs: https://www.postgresql.org/docs/
- spaCy Docs: https://spacy.io/
- scikit-learn Docs: https://scikit-learn.org/

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Built with**: Django, PostgreSQL, AI/NLP

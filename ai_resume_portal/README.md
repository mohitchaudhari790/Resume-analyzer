# AI Resume Analyzer & Job Matching Portal

A full-stack AI-powered job portal built with Django, PostgreSQL, and modern web technologies. Features include resume parsing, ATS scoring, AI job matching, and application tracking.

## 🚀 Features

### User Authentication
- User registration and login
- Password reset functionality
- Profile management with skills, education, and experience

### Resume Management
- Upload PDF/DOCX resumes
- AI-powered resume parsing
- Skill extraction using NLP
- ATS compatibility scoring
- Resume analysis with improvement suggestions

### Job Portal
- Browse and search jobs
- Filter by location, skills, and experience level
- Detailed job descriptions
- Save favorite jobs
- One-click job applications

### AI Features
- **Resume Analyzer**: ATS score, detected skills, missing skills, grammar suggestions
- **Job Matching**: AI-powered job recommendations based on resume
- **Skill Gap Analysis**: Identify missing skills for target jobs
- **Keyword Optimization**: Suggestions to improve resume visibility

### Application Tracking
- Track application status (Applied, Under Review, Interview, Selected, Rejected)
- Kanban-style application cards
- Match score for each application

### Admin Panel
- Post new jobs
- Manage job listings
- View user applications
- Full Django admin interface

## 🛠️ Tech Stack

**Backend:**
- Django 4.2.7
- PostgreSQL
- Python 3.8+

**Frontend:**
- HTML5
- CSS3 (with 3D animations and glassmorphism)
- JavaScript (ES6+)
- Font Awesome icons

**AI/NLP:**
- spaCy
- scikit-learn
- PyPDF2 (PDF parsing)
- python-docx (DOCX parsing)

## 📋 Prerequisites

- Python 3.8 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)

## 🔧 Installation & Setup

### 1. Clone or Navigate to Project Directory

```bash
cd "d:\mini project\ai_resume_portal"
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Download spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

### 6. Configure PostgreSQL Database

1. Install PostgreSQL if not already installed
2. Create a new database:

```sql
CREATE DATABASE ai_resume_db;
CREATE USER postgres WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE ai_resume_db TO postgres;
```

3. Update database credentials in `config/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ai_resume_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',  # Change this
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 7. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 9. Populate Sample Jobs (Optional)

```bash
python manage.py populate_jobs
```

This creates sample job listings for testing.

### 10. Run Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

## 📱 Usage Guide

### For Job Seekers

1. **Register**: Create an account at `/register/`
2. **Complete Profile**: Add your skills, education, and experience
3. **Upload Resume**: Upload your PDF/DOCX resume
4. **Get AI Analysis**: View your ATS score and improvement suggestions
5. **Browse Jobs**: Search and filter jobs by skills and location
6. **AI Job Match**: Get personalized job recommendations
7. **Apply**: Apply to jobs with one click
8. **Track Applications**: Monitor your application status

### For Employers (Admin)

1. **Login as Admin**: Use superuser credentials
2. **Access Admin Panel**: Visit `/admin/`
3. **Post Jobs**: Add new job listings with required skills
4. **Manage Applications**: View and update application statuses
5. **View Analytics**: Monitor user activity and applications

## 🎨 UI Features

- **Modern Gradient Design**: Purple/blue gradient backgrounds
- **3D CSS Animations**: Hover effects and card animations
- **Glassmorphism**: Frosted glass effect on cards
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Sidebar Navigation**: Easy access to all features
- **Progress Bars**: Visual representation of scores and matches
- **Status Badges**: Color-coded application statuses

## 📊 Database Schema

### Models

1. **Profile**: User profile with skills, education, experience
2. **Resume**: Uploaded resumes with parsed text and ATS score
3. **ExtractedSkill**: Skills extracted from resumes
4. **Job**: Job listings with requirements and details
5. **Application**: Job applications with status tracking
6. **SavedJob**: Bookmarked jobs
7. **ResumeAnalysis**: AI analysis results for resumes

## 🔐 Security Features

- CSRF protection
- Password hashing
- SQL injection prevention
- XSS protection
- Secure file uploads

## 🧪 Testing

To test the application:

1. Register a new user account
2. Upload a sample resume (PDF or DOCX)
3. View the AI analysis results
4. Browse job listings
5. Check AI job match recommendations
6. Apply to jobs and track applications

## 📁 Project Structure

```
ai_resume_portal/
├── config/                 # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── portal/                # Main application
│   ├── management/        # Custom management commands
│   ├── migrations/        # Database migrations
│   ├── admin.py          # Admin configuration
│   ├── ai_utils.py       # AI/NLP utilities
│   ├── forms.py          # Django forms
│   ├── models.py         # Database models
│   ├── urls.py           # App URL patterns
│   └── views.py          # View functions
├── templates/            # HTML templates
│   └── portal/
│       ├── base.html
│       ├── dashboard.html
│       ├── login.html
│       ├── register.html
│       └── ...
├── static/              # Static files
│   ├── css/
│   │   └── style.css   # Main stylesheet
│   └── js/
│       └── script.js   # JavaScript
├── media/              # User uploads
│   └── resumes/
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## 🚀 Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure allowed hosts
3. Set up a production database
4. Configure static files serving
5. Use a production server (Gunicorn, uWSGI)
6. Set up HTTPS with SSL certificate
7. Configure email backend for password reset

## 🤝 Contributing

This is a demonstration project. Feel free to fork and modify for your needs.

## 📝 License

This project is for educational purposes.

## 🐛 Troubleshooting

### Database Connection Error
- Ensure PostgreSQL is running
- Check database credentials in settings.py
- Verify database exists

### Module Not Found Error
- Activate virtual environment
- Install all requirements: `pip install -r requirements.txt`

### Static Files Not Loading
- Run: `python manage.py collectstatic`
- Check STATIC_URL and STATIC_ROOT in settings.py

### Resume Upload Error
- Ensure media directory exists
- Check file permissions
- Verify file format (PDF or DOCX only)

## 📧 Support

For issues or questions, please check the Django documentation or create an issue in the repository.

## 🎯 Future Enhancements

- Email notifications for application updates
- Video interview scheduling
- Company profiles
- Advanced analytics dashboard
- Resume builder tool
- Skill assessment tests
- Chat functionality between employers and candidates
- Mobile app version

---

**Built with ❤️ using Django and AI**

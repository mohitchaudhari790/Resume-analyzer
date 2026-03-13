# Resume Analyzer & Job Portal

A comprehensive Django-based job portal with AI-powered resume analysis, ATS scoring, and intelligent job matching.

## 🚀 Features

### Resume Analysis
- **ATS Score Calculation**: Analyze resumes against job descriptions with detailed scoring
- **Skill Extraction**: Automatic extraction of technical and soft skills using NLP
- **Visual Dashboard**: Interactive SVG-based score visualization
- **Improvement Suggestions**: AI-powered recommendations to improve resume quality

### Advanced Job Search
- **Smart Filters**: Search by location, job type, experience level, salary range, and skills
- **Real-time Matching**: Calculate match scores between your resume and job requirements
- **Skill Gap Analysis**: See matched skills and missing skills for each job
- **Posted Time Display**: Human-readable job posting timestamps

### AI-Powered Recommendations
- **Personalized Job Suggestions**: AI analyzes your profile and recommends best-fit jobs
- **Match Percentage**: See how well you match each recommended position
- **Skill Gap Insights**: Identify skills you need to develop for target roles

### Job Management
- **Save Jobs**: Bookmark interesting positions for later review
- **Application Tracking**: Track your job applications and their status
- **Company Details**: View comprehensive company information including website and industry

## 🛠️ Tech Stack

- **Backend**: Django 5.1.4, Python 3.12
- **Database**: PostgreSQL
- **NLP**: spaCy (en_core_web_sm)
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Render (Production-ready)
- **Static Files**: WhiteNoise
- **Server**: Gunicorn

## 📦 Installation

### Prerequisites
- Python 3.12+
- PostgreSQL
- Git

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/mohitchaudhari790/Resume-analyzer.git
cd Resume-analyzer
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

4. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your local settings
```

5. **Setup database**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to access the application.

## 🌐 Deployment

### Deploy to Render

1. **Push code to GitHub**
```bash
git push origin main
```

2. **Create Render account** at [render.com](https://render.com)

3. **Create PostgreSQL database**
   - Go to Dashboard → New → PostgreSQL
   - Note the Internal Database URL

4. **Create Web Service**
   - Go to Dashboard → New → Web Service
   - Connect your GitHub repository
   - Configure environment variables (see `.env.example`)

5. **Set environment variables** in Render dashboard:
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: False
   - `DATABASE_URL`: Your PostgreSQL URL
   - `ADMIN_URL`: Custom admin panel URL (e.g., secure-admin-2024)
   - `ALLOWED_HOSTS`: your-app.onrender.com

See `RENDER_DEPLOYMENT_GUIDE.md` for detailed deployment instructions.

## 📁 Project Structure

```
Resume-analyzer/
├── config/                 # Project settings
│   ├── settings.py        # Django settings with environment variables
│   ├── urls.py            # URL configuration with hidden admin
│   └── wsgi.py
├── portal/                # Main application
│   ├── models.py          # Job, Resume, Application models
│   ├── views.py           # Business logic and AI matching
│   ├── forms.py           # Advanced search forms
│   ├── templatetags/      # Custom template filters
│   └── templates/         # HTML templates
├── media/                 # User-uploaded files
├── static/                # CSS, JS, images
├── requirements.txt       # Python dependencies
├── build.sh              # Render build script
├── render.yaml           # Render configuration
└── .env.example          # Environment variables template
```

## 🔒 Security Features

- Hidden admin panel with custom URL
- Environment-based configuration
- CSRF and XSS protection
- Secure cookies in production
- SSL/HTTPS enforcement
- Database credentials in environment variables

## 🎯 Key Models

### Job Model
- Job type (Full-time, Part-time, Internship, Contract, Remote)
- Company details (name, website, description, industry)
- Salary range and experience requirements
- Skills required
- Posted time tracking

### Resume Model
- File upload and parsing
- Skill extraction
- ATS score calculation
- Match score with jobs

### Application Model
- Track job applications
- Application status
- Timestamps

## 🧪 Custom Template Filters

14 custom filters for advanced template rendering:
- `mul`, `div`, `sub`, `add` - Mathematical operations
- `percentage` - Calculate percentages
- `get_score_color` - Dynamic color coding
- `default_if_none` - Safe null handling
- And more...

## 📊 Admin Panel

Access admin panel at: `https://your-domain.com/<ADMIN_URL>/`

Default local: `http://localhost:8000/admin/`

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Mohit Chaudhari**
- GitHub: [@mohitchaudhari790](https://github.com/mohitchaudhari790)

## 🙏 Acknowledgments

- Django framework
- spaCy NLP library
- Render hosting platform
- Open source community

## 📧 Support

For issues and questions, please open an issue on GitHub.

---

Made with ❤️ by Mohit Chaudhari

# Complete Installation & Testing Guide

## 📋 Prerequisites Checklist

Before starting, ensure you have:

- [ ] Python 3.8 or higher installed
- [ ] PostgreSQL 12 or higher installed
- [ ] pip (Python package manager)
- [ ] Git (optional, for version control)
- [ ] Text editor or IDE (VS Code, PyCharm, etc.)
- [ ] Web browser (Chrome, Firefox, Edge)

## 🔧 Step-by-Step Installation

### Step 1: Verify Python Installation

```bash
python --version
# Should show Python 3.8 or higher

pip --version
# Should show pip version
```

### Step 2: Verify PostgreSQL Installation

```bash
psql --version
# Should show PostgreSQL version

# Test PostgreSQL connection
psql -U postgres
# Enter your PostgreSQL password
```

### Step 3: Create PostgreSQL Database

**Option A: Using psql command line**
```bash
psql -U postgres
```

Then run:
```sql
CREATE DATABASE ai_resume_db;
\q
```

**Option B: Using pgAdmin**
1. Open pgAdmin
2. Right-click on "Databases"
3. Select "Create" > "Database"
4. Name: `ai_resume_db`
5. Click "Save"

### Step 4: Navigate to Project Directory

```bash
cd "d:\mini project\ai_resume_portal"
```

### Step 5: Create Virtual Environment

```bash
python -m venv venv
```

This creates a `venv` folder in your project directory.

### Step 6: Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

You should see `(venv)` prefix in your command prompt.

**If activation fails on Windows:**
```bash
# Run PowerShell as Administrator
Set-ExecutionPolicy RemoteSigned

# Then try activating again
venv\Scripts\activate
```

### Step 7: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Django 4.2.7
- psycopg2-binary (PostgreSQL adapter)
- Pillow (Image processing)
- PyPDF2 (PDF parsing)
- pdfminer.six (Advanced PDF parsing)
- python-docx (DOCX parsing)
- spaCy (NLP)
- scikit-learn (Machine Learning)
- numpy, pandas (Data processing)
- nltk (Natural Language Toolkit)

**Installation may take 5-10 minutes.**

### Step 8: Download spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

This downloads the English language model for NLP tasks.

### Step 9: Configure Database Settings

Open `config/settings.py` and update the database configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ai_resume_db',
        'USER': 'postgres',
        'PASSWORD': 'YOUR_POSTGRESQL_PASSWORD',  # Change this!
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Step 10: Create Database Tables

```bash
# Create migration files
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate
```

You should see output like:
```
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying portal.0001_initial... OK
  ...
```

### Step 11: Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Enter the following when prompted:
- Username: `admin` (or your choice)
- Email: `admin@example.com`
- Password: (enter a secure password)
- Password (again): (confirm password)

**Remember these credentials!**

### Step 12: Populate Sample Jobs

```bash
python manage.py populate_jobs
```

This creates 6 sample job listings for testing.

### Step 13: Run Development Server

```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Step 14: Access the Application

Open your web browser and visit:
- **Main Site**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 🧪 Testing Guide

### Test 1: User Registration

1. Go to http://127.0.0.1:8000/register/
2. Fill in the registration form:
   - Username: `testuser`
   - First Name: `Test`
   - Last Name: `User`
   - Email: `test@example.com`
   - Password: `TestPass123!`
   - Confirm Password: `TestPass123!`
3. Click "Register"
4. You should be redirected to the dashboard

**Expected Result**: ✅ Account created, auto-logged in, dashboard displayed

### Test 2: Dashboard View

1. After login, you should see:
   - 4 stat cards (Resumes, Jobs, Applications, Saved Jobs)
   - Recent resumes section (empty initially)
   - Recent applications section (empty initially)
   - Quick action cards

**Expected Result**: ✅ Dashboard loads with all sections

### Test 3: Profile Settings

1. Click "Profile Settings" in sidebar
2. Fill in your profile:
   - Phone: `+1234567890`
   - City: `New York`
   - Skills: `Python, Django, JavaScript, React`
   - Education: `Bachelor's in Computer Science`
   - Experience: `2 years as Software Developer`
   - LinkedIn: `https://linkedin.com/in/testuser`
3. Click "Save Changes"

**Expected Result**: ✅ Profile updated successfully

### Test 4: Resume Upload

1. Click "Upload Resume" in sidebar
2. Prepare a test resume (PDF or DOCX)
   - If you don't have one, create a simple PDF with:
     - Your name
     - Skills: Python, Django, JavaScript
     - Experience: Software Developer
3. Click "Choose File" and select your resume
4. Click "Upload & Analyze"

**Expected Result**: ✅ Resume uploaded, redirected to analysis page

### Test 5: Resume Analysis

After uploading, you should see:
- ATS Score (0-100)
- Circular score visualization
- Detected Skills (tags)
- Missing Skills (tags)
- Improvement Suggestions (list)
- Keyword Suggestions (tags)

**Expected Result**: ✅ AI analysis displayed with all sections

### Test 6: Job Listings

1. Click "Job Listings" in sidebar
2. You should see 6 sample jobs:
   - Senior Python Django Developer
   - Frontend React Developer
   - AI/ML Engineer
   - Full Stack Developer Intern
   - DevOps Engineer
   - Data Scientist

**Expected Result**: ✅ All jobs displayed with details

### Test 7: Job Search & Filter

1. In the search box, type: `Python`
2. Click "Search"
3. You should see only Python-related jobs

4. Try location filter:
   - Location: `Remote`
   - Click "Search"

5. Try experience filter:
   - Select: `Senior Level`
   - Click "Search"

**Expected Result**: ✅ Filters work correctly

### Test 8: Job Details

1. Click "View Details" on any job
2. You should see:
   - Full job description
   - Required skills
   - Salary range
   - Match score (if resume uploaded)
   - Apply button
   - Save button

**Expected Result**: ✅ Job details page loads

### Test 9: Save Job

1. On job details page, click "Save Job"
2. Click "Saved Jobs" in sidebar
3. You should see the saved job

**Expected Result**: ✅ Job saved successfully

### Test 10: Apply to Job

1. Go to any job details page
2. Click "Apply for this Job"
3. You should see success message
4. Button changes to "Already Applied"

**Expected Result**: ✅ Application submitted

### Test 11: Application Tracker

1. Click "Applications" in sidebar
2. You should see your applied job with:
   - Job title and company
   - Status: "Applied"
   - Match score
   - Application date

**Expected Result**: ✅ Application tracked

### Test 12: AI Job Match

1. Click "AI Job Match" in sidebar
2. You should see:
   - Top matching jobs
   - Match percentage for each
   - Progress bars
   - Recommended jobs sorted by match score

**Expected Result**: ✅ AI recommendations displayed

### Test 13: Admin Panel (Staff Only)

1. Logout from regular user
2. Login with superuser credentials
3. Go to http://127.0.0.1:8000/admin/
4. You should see Django admin interface
5. Click on "Jobs" to manage job listings
6. Click on "Applications" to see all applications

**Expected Result**: ✅ Admin panel accessible

### Test 14: Add Job (Admin)

1. Login as admin/staff user
2. Click "Add Job" in sidebar (only visible to staff)
3. Fill in job details:
   - Title: `Test Job Position`
   - Company: `Test Company`
   - Location: `Test City`
   - Salary Min: `50000`
   - Salary Max: `80000`
   - Required Skills: `Python, Testing`
   - Experience Level: `Mid Level`
   - Description: `Test job description`
   - Deadline: (select future date)
4. Click "Post Job"

**Expected Result**: ✅ Job posted successfully

### Test 15: Password Reset

1. Logout
2. Go to login page
3. Click "Forgot Password?"
4. Enter your email
5. Check console output for reset link
6. Copy the reset link and paste in browser
7. Enter new password
8. Login with new password

**Expected Result**: ✅ Password reset works

### Test 16: Responsive Design

1. Open browser developer tools (F12)
2. Toggle device toolbar (Ctrl+Shift+M)
3. Test different screen sizes:
   - Mobile: 375px
   - Tablet: 768px
   - Desktop: 1920px

**Expected Result**: ✅ UI adapts to all screen sizes

### Test 17: Animations & Effects

1. Hover over cards - should lift up
2. Hover over buttons - should show depth
3. Watch score circle animate on analysis page
4. Watch progress bars animate
5. Watch skill tags fade in

**Expected Result**: ✅ All animations work smoothly

## 🐛 Troubleshooting

### Problem: "No module named 'django'"
**Solution**:
```bash
# Make sure virtual environment is activated
venv\Scripts\activate

# Reinstall requirements
pip install -r requirements.txt
```

### Problem: "FATAL: password authentication failed"
**Solution**:
```bash
# Check PostgreSQL password in config/settings.py
# Make sure it matches your PostgreSQL password
```

### Problem: "Port 8000 is already in use"
**Solution**:
```bash
# Use a different port
python manage.py runserver 8080

# Or find and kill the process using port 8000
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Problem: "Static files not loading"
**Solution**:
```bash
# Collect static files
python manage.py collectstatic --noinput

# Make sure DEBUG=True in settings.py for development
```

### Problem: "Resume upload fails"
**Solution**:
```bash
# Create media directory
mkdir media\resumes

# Check file permissions
# Make sure the file is PDF or DOCX
```

### Problem: "spaCy model not found"
**Solution**:
```bash
# Download the model again
python -m spacy download en_core_web_sm

# Or install directly
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.0/en_core_web_sm-3.7.0.tar.gz
```

## ✅ Verification Checklist

After installation, verify:

- [ ] Server runs without errors
- [ ] Can access homepage
- [ ] Can register new user
- [ ] Can login
- [ ] Dashboard displays correctly
- [ ] Can upload resume
- [ ] AI analysis works
- [ ] Can browse jobs
- [ ] Can apply to jobs
- [ ] Can save jobs
- [ ] Application tracker works
- [ ] AI job match works
- [ ] Profile settings work
- [ ] Admin panel accessible
- [ ] All pages load correctly
- [ ] No console errors
- [ ] Animations work
- [ ] Responsive design works

## 📊 Performance Benchmarks

Expected performance:
- Page load time: < 2 seconds
- Resume upload: < 5 seconds
- AI analysis: < 3 seconds
- Job search: < 1 second
- Database queries: < 100ms

## 🎓 Next Steps

After successful installation:

1. **Customize**: Update colors, logos, branding
2. **Add Content**: Add real job listings
3. **Configure Email**: Set up SMTP for password reset
4. **Deploy**: Deploy to production server
5. **Monitor**: Set up logging and monitoring
6. **Backup**: Configure database backups
7. **Scale**: Add caching, CDN, load balancing

## 📞 Getting Help

If you encounter issues:

1. Check this guide
2. Review README.md
3. Check Django documentation
4. Review error messages carefully
5. Check browser console for JavaScript errors
6. Check Django logs for backend errors

## 🎉 Success!

If all tests pass, congratulations! Your AI Resume Portal is fully functional.

You now have:
- ✅ Working authentication system
- ✅ AI-powered resume analysis
- ✅ Job portal with search and filters
- ✅ AI job matching system
- ✅ Application tracking
- ✅ Admin panel
- ✅ Modern, responsive UI

**Enjoy your AI Resume Portal!** 🚀

---

**Version**: 1.0.0  
**Last Updated**: 2024

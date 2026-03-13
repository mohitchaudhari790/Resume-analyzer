# 🔧 Render Deployment Fix

## Issue: Build Failed with Status 1

The build is failing because Render can't find the files in the correct location.

## ✅ Solution: Manual Configuration in Render Dashboard

### Step 1: Delete Current Service (if exists)
1. Go to Render Dashboard
2. Click your service → Settings → Delete Web Service

### Step 2: Create New Web Service
1. Click **"New +"** → **"Web Service"**
2. Connect repository: `mohitchaudhari790/Resume-analyzer`

### Step 3: Configure Settings

**Basic Settings:**
```
Name: ai-resume-portal
Region: Oregon (US West)
Branch: main
Root Directory: ai_resume_portal
Runtime: Python 3
```

**Build & Deploy:**
```
Build Command: 
pip install --upgrade pip && pip install -r requirements.txt && python -m spacy download en_core_web_sm && python manage.py collectstatic --no-input && python manage.py migrate

Start Command:
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
```

### Step 4: Environment Variables

Click **"Advanced"** → Add these variables:

```
SECRET_KEY = (click "Generate" button)
DEBUG = False
DATABASE_URL = postgresql://aidb_t5fe_user:yw1WOk7SlwrCJ6yRpjo7ALX3MLpu7cDN@dpg-d6oqp27kijhs73aup0j0-a.oregon-postgres.render.com/aidb_t5fe
ALLOWED_HOSTS = .onrender.com
ADMIN_URL = secure-admin-2024
RENDER = True
PYTHON_VERSION = 3.12.3
```

### Step 5: Deploy
Click **"Create Web Service"**

---

## Alternative: Use render.yaml (Blueprint)

If you want to use render.yaml instead:

1. Go to Render Dashboard
2. Click **"New +"** → **"Blueprint"**
3. Connect repository: `mohitchaudhari790/Resume-analyzer`
4. Render will detect `render.yaml` automatically
5. Add `DATABASE_URL` environment variable manually
6. Deploy

---

## 🐛 If Still Failing, Check Logs

In Render Dashboard → Your Service → Logs

Common errors:

### Error: "No such file or directory: requirements.txt"
**Fix:** Set `Root Directory` to `ai_resume_portal`

### Error: "Permission denied: build.sh"
**Fix:** Use the full build command (without build.sh):
```bash
pip install --upgrade pip && pip install -r requirements.txt && python -m spacy download en_core_web_sm && python manage.py collectstatic --no-input && python manage.py migrate
```

### Error: "ModuleNotFoundError"
**Fix:** Check requirements.txt exists in `ai_resume_portal/` folder

### Error: "Database connection failed"
**Fix:** Verify `DATABASE_URL` environment variable is set correctly

---

## 📋 Quick Copy-Paste Commands

**Build Command (Copy This):**
```bash
pip install --upgrade pip && pip install -r requirements.txt && python -m spacy download en_core_web_sm && python manage.py collectstatic --no-input && python manage.py migrate
```

**Start Command (Copy This):**
```bash
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
```

**Root Directory (Copy This):**
```
ai_resume_portal
```

---

## ✅ Expected Build Output

You should see:
```
==> Installing dependencies
Successfully installed Django-5.1.4 psycopg2-binary-2.9.10 ...

==> Downloading spaCy model
✔ Download and installation successful

==> Collecting static files
128 static files copied to '/opt/render/project/src/staticfiles'

==> Running migrations
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, portal, sessions
Running migrations:
  No migrations to apply.

==> Build successful!
```

---

## 🎯 After Successful Deployment

1. **Create Superuser:**
   - Go to Shell tab in Render
   - Run: `python manage.py createsuperuser`

2. **Access Your App:**
   - `https://your-app.onrender.com`

3. **Access Admin:**
   - `https://your-app.onrender.com/secure-admin-2024/`

---

## 💡 Pro Tip

If you keep getting errors, try deploying WITHOUT render.yaml:
1. Delete or rename `render.yaml` 
2. Use manual configuration in Render Dashboard
3. This gives you more control over the build process

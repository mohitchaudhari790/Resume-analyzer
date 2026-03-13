# 🏠 Local Setup Guide - Complete Solution

## ⚠️ ISSUE: PostgreSQL Not Installed

Your system doesn't have PostgreSQL installed. You have 2 options:

---

## ✅ OPTION 1: Use SQLite (EASIEST - No Installation Needed)

SQLite is built into Python - no installation required!

### Step 1: Update .env file

Open `d:\mini project\ai_resume_portal\.env` and change to:

```bash
# Django Settings
SECRET_KEY=django-insecure-local-dev-key-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration (SQLite - No installation needed)
# Leave DATABASE_URL commented out to use SQLite
# DATABASE_URL=

# Comment out PostgreSQL settings
# DB_ENGINE=django.db.backends.postgresql
# DB_NAME=ai_resume_db
# DB_USER=postgres
# DB_PASSWORD=postgre
# DB_HOST=localhost
# DB_PORT=5432

# Email Configuration (Development)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=localhost
EMAIL_PORT=1025
DEFAULT_FROM_EMAIL=noreply@airesumeportal.com

# Admin Panel Configuration
ADMIN_URL=admin
ADMIN_ENABLED=True

# Security Settings (Development)
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False
```

### Step 2: Update settings.py

The settings.py should automatically use SQLite when no DATABASE_URL is set.

### Step 3: Run Setup

```cmd
cd d:\mini project\ai_resume_portal
..\venv\Scripts\activate
python manage.py migrate
python create_test_user.py
python manage.py runserver
```

### Step 4: Access App

Open browser: `http://127.0.0.1:8000/login/`

Login with:
- Username: `testuser`
- Password: `testpass123`

---

## ✅ OPTION 2: Install PostgreSQL (Recommended for Production-like Setup)

### Step 1: Download PostgreSQL

1. Go to: https://www.postgresql.org/download/windows/
2. Download PostgreSQL 16 (or latest version)
3. Run the installer

### Step 2: Installation Settings

During installation:
- **Password:** Set to `postgre` (or remember what you set)
- **Port:** 5432 (default)
- **Locale:** Default
- Install all components including pgAdmin

### Step 3: Add PostgreSQL to PATH

1. Open System Environment Variables
2. Edit PATH variable
3. Add: `C:\Program Files\PostgreSQL\16\bin`
4. Click OK and restart terminal

### Step 4: Verify Installation

```cmd
psql --version
```

Should show: `psql (PostgreSQL) 16.x`

### Step 5: Create Database

```cmd
cd d:\mini project\ai_resume_portal
setup_complete.bat
```

This will:
- Create database `ai_resume_db`
- Run migrations
- Setup everything

### Step 6: Start Server

```cmd
python create_test_user.py
python manage.py runserver
```

---

## 🚀 QUICK START (Using SQLite - Recommended for Now)

Just run these commands:

```cmd
cd d:\mini project\ai_resume_portal
..\venv\Scripts\activate
python manage.py migrate
python create_test_user.py
python manage.py runserver
```

Then open: `http://127.0.0.1:8000/login/`

---

## 📊 Database Comparison

| Feature | SQLite | PostgreSQL |
|---------|--------|------------|
| Installation | ✅ Built-in | ❌ Requires install |
| Setup Time | ⚡ Instant | 🕐 10-15 minutes |
| Performance | ✅ Good for dev | ✅ Better for production |
| File-based | ✅ Yes (db.sqlite3) | ❌ No (server-based) |
| Recommended for | 🏠 Local development | 🌐 Production & Local |

---

## 🔧 Current Configuration Status

### Your .env file is set to:
- ✅ DEBUG=True (Local mode)
- ✅ ALLOWED_HOSTS=localhost,127.0.0.1
- ❌ DATABASE_URL pointing to Render (needs to be commented out)
- ❌ Local PostgreSQL settings (PostgreSQL not installed)

### What needs to change:
1. Comment out `DATABASE_URL` line
2. Comment out PostgreSQL settings (DB_ENGINE, DB_NAME, etc.)
3. Django will automatically use SQLite

---

## 🎯 Recommended Solution for You

**Use SQLite for local development:**

1. It's already installed with Python
2. No configuration needed
3. Perfect for development
4. Easy to switch to PostgreSQL later

**When to use PostgreSQL:**
- When you need production-like environment
- When testing database-specific features
- When you have PostgreSQL installed

---

## 📝 Complete Setup Commands (SQLite)

```cmd
REM Navigate to project
cd d:\mini project\ai_resume_portal

REM Activate virtual environment
..\venv\Scripts\activate

REM Run migrations (creates db.sqlite3)
python manage.py migrate

REM Create test user
python create_test_user.py

REM Start server
python manage.py runserver
```

---

## 🐛 Troubleshooting

### Error: "No module named 'psycopg2'"
**Solution:** You're trying to use PostgreSQL but it's not installed. Use SQLite instead (comment out DATABASE_URL in .env)

### Error: "could not connect to server"
**Solution:** PostgreSQL is not running or not installed. Use SQLite instead.

### Error: "FATAL: password authentication failed"
**Solution:** Wrong PostgreSQL password. Either:
1. Use SQLite (easier)
2. Reset PostgreSQL password to 'postgre'

---

## ✅ What I'll Do Now

I'll update your .env file to use SQLite so you can run locally immediately!

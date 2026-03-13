@echo off
echo ========================================
echo AI Resume Portal - Local Setup
echo ========================================
echo.

REM Set PostgreSQL password
set PGPASSWORD=postgre

echo [Step 1/6] Checking PostgreSQL...
psql -U postgres -c "SELECT version();" >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Cannot connect to PostgreSQL!
    echo.
    echo Please ensure:
    echo 1. PostgreSQL is installed
    echo 2. PostgreSQL service is running
    echo 3. Password for 'postgres' user is 'postgre'
    echo.
    echo To set password, run in psql:
    echo ALTER USER postgres PASSWORD 'postgre';
    echo.
    pause
    exit /b 1
)
echo [OK] PostgreSQL is running

echo.
echo [Step 2/6] Creating database...
psql -U postgres -c "DROP DATABASE IF EXISTS ai_resume_db;" >nul 2>&1
psql -U postgres -c "CREATE DATABASE ai_resume_db;" >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Failed to create database!
    pause
    exit /b 1
)
echo [OK] Database 'ai_resume_db' created

echo.
echo [Step 3/6] Activating virtual environment...
if not exist "..\venv\Scripts\activate.bat" (
    echo [ERROR] Virtual environment not found!
    echo Creating virtual environment...
    cd ..
    python -m venv venv
    cd ai_resume_portal
)
call ..\venv\Scripts\activate.bat
echo [OK] Virtual environment activated

echo.
echo [Step 4/6] Installing dependencies...
pip install -q -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies!
    pause
    exit /b 1
)
echo [OK] Dependencies installed

echo.
echo [Step 5/6] Downloading spaCy model...
python -m spacy download en_core_web_sm >nul 2>&1
echo [OK] spaCy model downloaded

echo.
echo [Step 6/6] Running migrations...
python manage.py migrate
if %errorlevel% neq 0 (
    echo [ERROR] Migration failed!
    pause
    exit /b 1
)
echo [OK] Migrations completed

echo.
echo ========================================
echo SUCCESS! Setup Complete!
echo ========================================
echo.
echo Database Configuration:
echo   Database: ai_resume_db
echo   User: postgres
echo   Password: postgre
echo   Host: localhost
echo   Port: 5432
echo.
echo Next Steps:
echo   1. Create test user: python create_test_user.py
echo   2. Start server: python manage.py runserver
echo   3. Open browser: http://127.0.0.1:8000
echo.
echo ========================================
pause

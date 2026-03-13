@echo off
cls
echo ========================================
echo   AI Resume Portal - Quick Start
echo ========================================
echo.

cd /d "%~dp0"

echo [1/5] Activating virtual environment...
if not exist "..\venv\Scripts\activate.bat" (
    echo [ERROR] Virtual environment not found!
    echo Please run: python -m venv ..\venv
    pause
    exit /b 1
)
call ..\venv\Scripts\activate.bat
echo [OK] Virtual environment activated
echo.

echo [2/5] Checking Django installation...
python -c "import django" 2>nul
if %errorlevel% neq 0 (
    echo [INSTALLING] Installing dependencies...
    pip install -q -r requirements.txt
    python -m spacy download en_core_web_sm
)
echo [OK] Django is installed
echo.

echo [3/5] Running migrations...
python manage.py migrate --noinput
if %errorlevel% neq 0 (
    echo [ERROR] Migration failed!
    pause
    exit /b 1
)
echo [OK] Database ready
echo.

echo [4/5] Checking for test user...
python -c "from django.contrib.auth.models import User; import django; import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings'); django.setup(); exit(0 if User.objects.filter(username='testuser').exists() else 1)" 2>nul
if %errorlevel% neq 0 (
    echo [CREATING] Creating test user...
    python create_test_user.py
)
echo [OK] Test user ready
echo.

echo [5/5] Starting development server...
echo.
echo ========================================
echo   Server Starting...
echo ========================================
echo.
echo   URL: http://127.0.0.1:8000
echo   Login: http://127.0.0.1:8000/login/
echo.
echo   Test Credentials:
echo   Username: testuser
echo   Password: testpass123
echo.
echo   Press CTRL+C to stop the server
echo ========================================
echo.

python manage.py runserver

pause

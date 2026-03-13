@echo off
echo ========================================
echo AI Resume Portal - Quick Setup
echo ========================================
echo.

echo [1/7] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

echo [2/7] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/7] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo [4/7] Downloading spaCy model...
python -m spacy download en_core_web_sm

echo [5/7] Running migrations...
python manage.py makemigrations
python manage.py migrate

echo [6/7] Creating superuser...
echo Please create an admin account:
python manage.py createsuperuser

echo [7/7] Populating sample jobs...
python manage.py populate_jobs

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To start the server, run:
echo   venv\Scripts\activate
echo   python manage.py runserver
echo.
echo Then visit: http://127.0.0.1:8000/
echo Admin panel: http://127.0.0.1:8000/admin/
echo.
pause

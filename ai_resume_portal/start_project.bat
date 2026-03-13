@echo off
echo ========================================
echo Starting AI Resume Portal
echo ========================================
echo.

echo [1/3] Activating virtual environment...
call ..\venv\Scripts\activate.bat

echo.
echo [2/3] Checking Django configuration...
python manage.py check

echo.
echo [3/3] Starting development server...
echo.
echo ========================================
echo Server will start at: http://127.0.0.1:8000
echo Press CTRL+C to stop the server
echo ========================================
echo.

python manage.py runserver

pause

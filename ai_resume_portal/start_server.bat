@echo off
echo ========================================
echo AI Resume Portal - Starting Server
echo ========================================
echo.

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Starting Django development server...
echo.
echo Server will be available at: http://127.0.0.1:8000/
echo Admin panel at: http://127.0.0.1:8000/admin/
echo.
echo Login credentials:
echo Username: admin
echo Password: admin123
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver

pause

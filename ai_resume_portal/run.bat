@echo off
echo Starting AI Resume Portal...
echo.

call venv\Scripts\activate.bat

echo Server starting at http://127.0.0.1:8000/
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver

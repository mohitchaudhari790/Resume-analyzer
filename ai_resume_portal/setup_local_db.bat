@echo off
echo ========================================
echo Setting Up Local PostgreSQL Database
echo ========================================
echo.

echo [1/5] Checking PostgreSQL connection...
psql -U postgres -c "SELECT version();" 2>nul
if %errorlevel% neq 0 (
    echo ERROR: Cannot connect to PostgreSQL!
    echo Please make sure:
    echo 1. PostgreSQL is installed
    echo 2. PostgreSQL service is running
    echo 3. Password is set to 'postgre'
    echo.
    pause
    exit /b 1
)

echo.
echo [2/5] Dropping existing database (if exists)...
psql -U postgres -c "DROP DATABASE IF EXISTS ai_resume_db;" 2>nul

echo.
echo [3/5] Creating new database...
psql -U postgres -c "CREATE DATABASE ai_resume_db;"
if %errorlevel% neq 0 (
    echo ERROR: Failed to create database!
    pause
    exit /b 1
)

echo.
echo [4/5] Verifying database...
psql -U postgres -c "\l" | findstr ai_resume_db
if %errorlevel% neq 0 (
    echo ERROR: Database not found!
    pause
    exit /b 1
)

echo.
echo [5/5] Running Django migrations...
cd /d "%~dp0"
call ..\venv\Scripts\activate.bat
python manage.py migrate

echo.
echo ========================================
echo SUCCESS! Local database is ready!
echo ========================================
echo.
echo Database: ai_resume_db
echo User: postgres
echo Password: postgre
echo Host: localhost
echo Port: 5432
echo.
echo Next steps:
echo 1. Create a user: python create_test_user.py
echo 2. Start server: python manage.py runserver
echo.
pause

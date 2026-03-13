-- PostgreSQL Database Setup Script
-- Run this script in PostgreSQL to create the database

-- Create database
CREATE DATABASE ai_resume_db;

-- Create user (if not exists)
-- Note: Change 'your_password' to a secure password
DO
$do$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_roles
      WHERE  rolname = 'postgres') THEN
      CREATE USER postgres WITH PASSWORD 'your_password';
   END IF;
END
$do$;

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE ai_resume_db TO postgres;

-- Connect to the database
\c ai_resume_db

-- Grant schema privileges
GRANT ALL ON SCHEMA public TO postgres;

-- Success message
SELECT 'Database ai_resume_db created successfully!' AS status;

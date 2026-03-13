"""
Create a test user for login testing
Run: python create_test_user.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from portal.models import Profile

def create_test_user():
    # Check if user already exists
    if User.objects.filter(username='testuser').exists():
        print("❌ Test user 'testuser' already exists!")
        print("\nLogin Credentials:")
        print("Username: testuser")
        print("Password: testpass123")
        return
    
    # Create test user
    user = User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123',
        first_name='Test',
        last_name='User'
    )
    
    # Create profile
    Profile.objects.create(user=user)
    
    print("✅ Test user created successfully!")
    print("\n" + "="*50)
    print("LOGIN CREDENTIALS:")
    print("="*50)
    print("Username: testuser")
    print("Password: testpass123")
    print("="*50)
    print("\nYou can now login at: http://127.0.0.1:8000/login/")

if __name__ == '__main__':
    create_test_user()

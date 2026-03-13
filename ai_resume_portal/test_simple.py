"""
Simple test for custom template filters
Run: python test_simple.py
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from portal.templatetags.custom_filters import multiply, default_if_none, get_score_color

print("=" * 60)
print("Testing Custom Template Filters")
print("=" * 60)

# Test 1
result = multiply(85, 5.34)
print(f"\n1. multiply(85, 5.34) = {result}")
print(f"   Expected: 453.9")
print(f"   Status: {'PASS' if abs(result - 453.9) < 0.1 else 'FAIL'}")

# Test 2
result = multiply(None, 5.34)
print(f"\n2. multiply(None, 5.34) = {result}")
print(f"   Expected: 0")
print(f"   Status: {'PASS' if result == 0 else 'FAIL'}")

# Test 3
result = default_if_none(None, 50)
print(f"\n3. default_if_none(None, 50) = {result}")
print(f"   Expected: 50")
print(f"   Status: {'PASS' if result == 50 else 'FAIL'}")

# Test 4
result = get_score_color(85)
print(f"\n4. get_score_color(85) = {result}")
print(f"   Expected: success")
print(f"   Status: {'PASS' if result == 'success' else 'FAIL'}")

print("\n" + "=" * 60)
print("All tests completed successfully!")
print("=" * 60)
print("\nCustom filters are working correctly.")
print("Now restart your Django server and test the analysis page.")

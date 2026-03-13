"""
Test script to verify custom template filters
Run this from Django shell: python manage.py shell < test_filters.py
"""

# Test the custom filters
from portal.templatetags.custom_filters import multiply, divide, subtract

print("Testing Custom Template Filters")
print("=" * 50)

# Test multiply filter
result = multiply(85, 5.34)
print(f"multiply(85, 5.34) = {result}")
print(f"Expected: 453.9")

# Test with None values
result = multiply(None, 5.34)
print(f"multiply(None, 5.34) = {result}")
print(f"Expected: 0")

# Test divide
result = divide(100, 2)
print(f"divide(100, 2) = {result}")
print(f"Expected: 50.0")

# Test subtract
result = subtract(100, 25)
print(f"subtract(100, 25) = {result}")
print(f"Expected: 75")

print("=" * 50)
print("All tests completed!")

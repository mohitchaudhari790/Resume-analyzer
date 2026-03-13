"""
Django management command to verify custom template filters
Usage: python manage.py verify_filters
"""
from django.core.management.base import BaseCommand
from django.template import Template, Context
from portal.templatetags import custom_filters

class Command(BaseCommand):
    help = 'Verify custom template filters are working correctly'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(self.style.SUCCESS('Testing Custom Template Filters'))
        self.stdout.write(self.style.SUCCESS('=' * 60))
        
        # Test 1: Multiply filter
        self.stdout.write('\n1. Testing multiply filter (mul):')
        result = custom_filters.multiply(85, 5.34)
        self.stdout.write(f'   multiply(85, 5.34) = {result}')
        self.stdout.write(f'   Expected: 453.9')
        if abs(result - 453.9) < 0.1:
            self.stdout.write(self.style.SUCCESS('   ✓ PASS'))
        else:
            self.stdout.write(self.style.ERROR('   ✗ FAIL'))
        
        # Test 2: Null handling
        self.stdout.write('\n2. Testing null value handling:')
        result = custom_filters.multiply(None, 5.34)
        self.stdout.write(f'   multiply(None, 5.34) = {result}')
        self.stdout.write(f'   Expected: 0')
        if result == 0:
            self.stdout.write(self.style.SUCCESS('   ✓ PASS'))
        else:
            self.stdout.write(self.style.ERROR('   ✗ FAIL'))
        
        # Test 3: Default if none
        self.stdout.write('\n3. Testing default_if_none filter:')
        result = custom_filters.default_if_none(None, 50)
        self.stdout.write(f'   default_if_none(None, 50) = {result}')
        self.stdout.write(f'   Expected: 50')
        if result == 50:
            self.stdout.write(self.style.SUCCESS('   ✓ PASS'))
        else:
            self.stdout.write(self.style.ERROR('   ✗ FAIL'))
        
        # Test 4: Get score color
        self.stdout.write('\n4. Testing get_score_color filter:')
        result = custom_filters.get_score_color(85)
        self.stdout.write(f'   get_score_color(85) = {result}')
        self.stdout.write(f'   Expected: success')
        if result == 'success':
            self.stdout.write(self.style.SUCCESS('   ✓ PASS'))
        else:
            self.stdout.write(self.style.ERROR('   ✗ FAIL'))
        
        # Test 5: Template rendering
        self.stdout.write('\n5. Testing template rendering:')
        try:
            template_string = """
            {% load custom_filters %}
            {{ score|default_if_none:0|mul:5.34 }}
            """
            template = Template(template_string)
            context = Context({'score': 85})
            result = template.render(context).strip()
            self.stdout.write(f'   Template result: {result}')
            self.stdout.write(f'   Expected: 453.9')
            if abs(float(result) - 453.9) < 0.1:
                self.stdout.write(self.style.SUCCESS('   ✓ PASS'))
            else:
                self.stdout.write(self.style.ERROR('   ✗ FAIL'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'   ✗ FAIL: {str(e)}'))
        
        # Test 6: Percentage calculation
        self.stdout.write('\n6. Testing percentage filter:')
        result = custom_filters.percentage(8, 10)
        self.stdout.write(f'   percentage(8, 10) = {result}')
        self.stdout.write(f'   Expected: 80.0')
        if result == 80.0:
            self.stdout.write(self.style.SUCCESS('   ✓ PASS'))
        else:
            self.stdout.write(self.style.ERROR('   ✗ FAIL'))
        
        # Summary
        self.stdout.write('\n' + '=' * 60)
        self.stdout.write(self.style.SUCCESS('All tests completed!'))
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write('\nNext steps:')
        self.stdout.write('1. Restart Django server: python manage.py runserver')
        self.stdout.write('2. Upload a resume and check analysis page')
        self.stdout.write('3. Verify ATS score circle displays correctly')
        self.stdout.write('\n')

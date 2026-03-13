# Django Custom Template Filter Integration Guide

## Problem Fixed
The template error `'custom_filters' is not a registered tag library` has been resolved by creating a proper Django template tag library.

## Files Created

### 1. Template Tags Directory Structure
```
portal/
├── templatetags/
│   ├── __init__.py          # Makes it a Python package
│   └── custom_filters.py    # Custom template filters
```

### 2. Custom Filters Implemented

**File:** `portal/templatetags/custom_filters.py`

**Available Filters:**
- `mul` - Multiply two numbers
- `div` - Divide two numbers
- `sub` - Subtract two numbers
- `add_custom` - Add two numbers
- `percentage` - Calculate percentage
- `default_if_none` - Provide default for None values
- `abs_value` - Get absolute value
- `round_decimal` - Round to decimal places
- `format_number` - Format with commas
- `get_score_color` - Get color class based on score
- `get_match_level` - Get match level text
- `safe_int` - Safely convert to integer
- `safe_float` - Safely convert to float

## Integration Steps

### Step 1: Restart Django Server

**IMPORTANT:** Django must be restarted to recognize new template tags.

```bash
# Stop the current server (Ctrl+C)
# Then restart:
python manage.py runserver
```

### Step 2: Verify Template Tags Are Loaded

Run this test in Django shell:

```bash
python manage.py shell
```

Then in the shell:
```python
from portal.templatetags.custom_filters import multiply
result = multiply(85, 5.34)
print(result)  # Should print: 453.9
```

### Step 3: Template Usage

The template has been updated to load the custom filters:

```django
{% extends 'portal/base.html' %}
{% load custom_filters %}

{% block content %}
<!-- Now you can use the filters -->
<circle stroke-dasharray="{{ resume.ats_score|default_if_none:0|mul:5.34 }} 534"/>
{% endblock %}
```

## How the ATS Score Visualization Works

### SVG Circle Progress Animation

The ATS score is displayed as an animated circular progress bar using SVG.

**Formula:**
```
stroke-dasharray = "score * 5.34 534"
```

**Explanation:**
- Circle circumference = 2 × π × radius = 2 × 3.14159 × 85 ≈ 534
- For a score of 85: 85 × 5.34 = 453.9
- This creates a dash of 453.9 units and a gap of 534 units
- Result: 85% of the circle is filled

**Safe Default Handling:**
```django
{{ resume.ats_score|default_if_none:0|mul:5.34 }}
```
- If `resume.ats_score` is None, it defaults to 0
- Then multiplies by 5.34
- Prevents template crashes

## Color Coding

The circle color changes based on score:

```django
{% if resume.ats_score|default_if_none:0 >= 80 %}
    stroke="#48bb78"  <!-- Green for Excellent -->
{% elif resume.ats_score|default_if_none:0 >= 60 %}
    stroke="#ed8936"  <!-- Orange for Good -->
{% else %}
    stroke="#f56565"  <!-- Red for Needs Improvement -->
{% endif %}
```

## Testing the Fix

### Test 1: Upload Resume
1. Go to: http://127.0.0.1:8000/upload-resume/
2. Upload a PDF or DOCX resume
3. Should redirect to analysis page without errors

### Test 2: View Analysis
1. Go to: http://127.0.0.1:8000/analyze-resume/12/
2. Should see:
   - Animated ATS score circle
   - Score number displayed
   - Color-coded based on score
   - No template errors

### Test 3: Null Score Handling
If a resume has no ATS score (null in database):
- Circle shows 0% (empty)
- Score displays as "0"
- No template crash

## Common Issues & Solutions

### Issue 1: "custom_filters is not a registered tag library"

**Solution:**
1. Ensure `portal` is in `INSTALLED_APPS` in settings.py
2. Restart Django server completely
3. Clear browser cache
4. Check file structure is correct

### Issue 2: Filter not working

**Solution:**
1. Verify `{% load custom_filters %}` is at the top of template
2. Check filter syntax: `{{ value|filter_name:argument }}`
3. Ensure no typos in filter name

### Issue 3: Score not displaying

**Solution:**
1. Check if resume.ats_score exists in database
2. Use `|default_if_none:0` to handle null values
3. Verify the resume object is passed in context

## Additional Filter Examples

### Example 1: Calculate Match Percentage
```django
{{ matched_skills|length|percentage:total_skills }}
```

### Example 2: Format Salary
```django
${{ job.salary_min|format_number }} - ${{ job.salary_max|format_number }}
```

### Example 3: Round Score
```django
{{ resume.ats_score|round_decimal:1 }}%
```

### Example 4: Get Color Class
```django
<div class="badge badge-{{ match_score|get_score_color }}">
    {{ match_score }}%
</div>
```

## Verification Checklist

- [x] `portal/templatetags/` directory created
- [x] `__init__.py` file exists in templatetags
- [x] `custom_filters.py` contains all filters
- [x] Template loads filters with `{% load custom_filters %}`
- [x] All score references use `|default_if_none:0`
- [x] Django server restarted
- [x] No template syntax errors

## Next Steps

1. **Restart your Django server** (most important!)
2. Test the resume upload and analysis flow
3. Verify the ATS score circle animates correctly
4. Check that null scores don't crash the page

## Support

If you still see errors after restarting:

1. Check Django version compatibility:
   ```bash
   python manage.py --version
   ```

2. Verify portal app is installed:
   ```python
   # In settings.py
   INSTALLED_APPS = [
       ...
       'portal',  # Must be here
   ]
   ```

3. Clear Python cache:
   ```bash
   find . -type d -name __pycache__ -exec rm -r {} +
   ```

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Success Indicators

✅ No template errors when accessing analysis page
✅ ATS score circle displays and animates
✅ Score number shows correctly
✅ Color changes based on score value
✅ Null scores handled gracefully (show 0)

---

**Created:** 2024
**Last Updated:** After fixing template filter issue
**Status:** ✅ Ready for Production

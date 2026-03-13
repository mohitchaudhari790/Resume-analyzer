"""
Custom Django Template Filters
Provides mathematical and utility filters for templates
"""
from django import template
from decimal import Decimal, InvalidOperation

register = template.Library()

@register.filter(name='mul')
def multiply(value, arg):
    """
    Multiplies the value by the argument
    Usage: {{ value|mul:5 }}
    """
    try:
        # Convert to float for calculation
        value = float(value) if value is not None else 0
        arg = float(arg) if arg is not None else 0
        result = value * arg
        return result
    except (ValueError, TypeError, InvalidOperation):
        # Return 0 if conversion fails
        return 0

@register.filter(name='div')
def divide(value, arg):
    """
    Divides the value by the argument
    Usage: {{ value|div:2 }}
    """
    try:
        value = float(value) if value is not None else 0
        arg = float(arg) if arg is not None else 1
        if arg == 0:
            return 0
        result = value / arg
        return result
    except (ValueError, TypeError, InvalidOperation):
        return 0

@register.filter(name='sub')
def subtract(value, arg):
    """
    Subtracts the argument from the value
    Usage: {{ value|sub:10 }}
    """
    try:
        value = float(value) if value is not None else 0
        arg = float(arg) if arg is not None else 0
        result = value - arg
        return result
    except (ValueError, TypeError, InvalidOperation):
        return 0

@register.filter(name='add_custom')
def add_custom(value, arg):
    """
    Adds the argument to the value (custom implementation)
    Usage: {{ value|add_custom:5 }}
    """
    try:
        value = float(value) if value is not None else 0
        arg = float(arg) if arg is not None else 0
        result = value + arg
        return result
    except (ValueError, TypeError, InvalidOperation):
        return 0

@register.filter(name='percentage')
def percentage(value, total):
    """
    Calculates percentage
    Usage: {{ value|percentage:total }}
    """
    try:
        value = float(value) if value is not None else 0
        total = float(total) if total is not None else 1
        if total == 0:
            return 0
        result = (value / total) * 100
        return round(result, 2)
    except (ValueError, TypeError, InvalidOperation):
        return 0

@register.filter(name='default_if_none')
def default_if_none(value, default):
    """
    Returns default value if value is None
    Usage: {{ value|default_if_none:0 }}
    """
    return value if value is not None else default

@register.filter(name='abs_value')
def absolute_value(value):
    """
    Returns absolute value
    Usage: {{ value|abs_value }}
    """
    try:
        value = float(value) if value is not None else 0
        return abs(value)
    except (ValueError, TypeError):
        return 0

@register.filter(name='round_decimal')
def round_decimal(value, places=2):
    """
    Rounds to specified decimal places
    Usage: {{ value|round_decimal:2 }}
    """
    try:
        value = float(value) if value is not None else 0
        places = int(places) if places is not None else 2
        return round(value, places)
    except (ValueError, TypeError):
        return 0

@register.filter(name='format_number')
def format_number(value):
    """
    Formats number with commas
    Usage: {{ value|format_number }}
    """
    try:
        value = float(value) if value is not None else 0
        return "{:,.0f}".format(value)
    except (ValueError, TypeError):
        return "0"

@register.filter(name='get_score_color')
def get_score_color(score):
    """
    Returns color class based on score
    Usage: {{ score|get_score_color }}
    """
    try:
        score = float(score) if score is not None else 0
        if score >= 80:
            return 'success'
        elif score >= 60:
            return 'warning'
        else:
            return 'danger'
    except (ValueError, TypeError):
        return 'secondary'

@register.filter(name='get_match_level')
def get_match_level(score):
    """
    Returns match level text based on score
    Usage: {{ score|get_match_level }}
    """
    try:
        score = float(score) if score is not None else 0
        if score >= 80:
            return 'Excellent Match'
        elif score >= 60:
            return 'Good Match'
        elif score >= 40:
            return 'Moderate Match'
        else:
            return 'Low Match'
    except (ValueError, TypeError):
        return 'No Match'

@register.filter(name='safe_int')
def safe_int(value, default=0):
    """
    Safely converts value to integer
    Usage: {{ value|safe_int:0 }}
    """
    try:
        return int(value) if value is not None else default
    except (ValueError, TypeError):
        return default

@register.filter(name='safe_float')
def safe_float(value, default=0.0):
    """
    Safely converts value to float
    Usage: {{ value|safe_float:0.0 }}
    """
    try:
        return float(value) if value is not None else default
    except (ValueError, TypeError):
        return default

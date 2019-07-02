"""
https://docs.djangoproject.com/en/2.1/howto/custom-template-tags/

The app should contain a templatetags directory, at the same level as models.py, views.py, etc.
If this doesn’t already exist, create it - don’t forget the __init__.py file to ensure
the directory is treated as a Python package.

polls/
    __init__.py
    models.py
    templatetags/
        __init__.py
        poll_extras.py
    views.p

And in your template you would use the following:

{% load poll_extras %}
"""

from django import template
register = template.Library()

# basic - add class
@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})

# advance - add attr
@register.filter(name='add_attr')
def add_attr(field, css):
    attrs = {}
    definition = css.split(',')

    for d in definition:
        if ':' not in d:
            attrs['class'] = d
        else:
            key, val = d.split(':')
            attrs[key] = val

    return field.as_widget(attrs=attrs)

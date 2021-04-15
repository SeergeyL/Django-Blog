from django import template


register = template.Library()


@register.filter
def addclass(field, css):
    """Adds :css: class to field"""

    return field.as_widget(attrs={"class": css})


@register.simple_tag
def style_form_field(field, **kwargs):
    """
    Allows to add attributes to specified field

    Usage:
    {% style_form_field form.field class="form-control" placeholder="Enter username" %}
    """
    return field.as_widget(attrs=kwargs)
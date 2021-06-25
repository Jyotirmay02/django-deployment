from django import template

register = template.Library()

@register.filter(name = "cut")
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')


# Instead of this we can use decorators
# register.filter('cut',cut)
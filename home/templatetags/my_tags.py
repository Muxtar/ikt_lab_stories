from atexit import register
from django.template import Library
from home.models import Category

register = Library()

@register.simple_tag
def category_global():
    categories = Category.objects.all()
    return categories
from django.template import Library
from django import template

register = template.Library()

from app.models import *

def Header():
    return {}
register.inclusion_tag('tags/header.html')(Header)

def Footer():
    return {}
register.inclusion_tag('tags/footer.html')(Footer)

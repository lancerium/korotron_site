from django import template
from django.db.models import Count, F

from korotron.models import CategoryService

register = template.Library()


@register.inclusion_tag('main/navbar.html')
def show_categories():
    categories = CategoryService.objects.annotate(cnt=Count('services', filter=F('services__is_published'))).filter(cnt__gt=0)
    return {'categories': categories,}
from itertools import chain
from django import template
from svarmeh.models import Page, Product, Chunk
from django.core.cache import cache

register = template.Library()


@register.inclusion_tag('include/menu.html', takes_context=True)
def main_menu(context):
    products = Product.objects.filter(status='published')
    pages = Page.objects.filter(status='published', in_menu=True).order_by('weight')

    for p in chain(pages, products):
        p.url = p.get_absolute_url()

    return {
        'products': products,
        'pages': pages,
        'path': context['request'].path,
        'in_products': context['request'].path.startswith('/products/'),
    }

@register.simple_tag
def chunk(key):
    try:
        cache_key = 'chunk-' + key
        c = cache.get(cache_key)
        if c is None:
            c = Chunk.objects.get(key=key)
            cache.set(cache_key, c)
        return c.content
    except Chunk.DoesNotExist:
        return ''

@register.filter
def half(number):
    return number / 2


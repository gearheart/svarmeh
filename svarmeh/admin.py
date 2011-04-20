# -*- coding: utf-8 -*-

from django.contrib import admin
from svarmeh.models import Product, Page, Chunk
from redactor.admin import RedactorModelAdmin

class ProductAdmin(RedactorModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'image', 'intro', 'description', 'status')
        }),
        (u'Дополнительно', {
            'classes': ('collapse',),
            'fields': ('slug', )
        }),
    )

class PageAdmin(RedactorModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'in_menu', 'body', 'status')
        }),
        (u'Дополнительно', {
            'classes': ('collapse',),
            'fields': ('slug', 'weight', )
        }),
    )

class ChunkAdmin(admin.ModelAdmin):
  list_display = ('key', 'content')

admin.site.register(Chunk, ChunkAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Product, ProductAdmin)


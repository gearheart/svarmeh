# -*- coding: utf-8 -*-

from django.contrib import admin
from svarmeh.models import Product, Page, Chunk, MainPageBlock
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

    hidden = ('status', 'in_menu', 'slug', 'weight')
    readonly = ('title', )

    def has_delete_permission(self, request, obj=None):
        return bool(obj) and obj.slug != '/'

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.slug == '/':
            return self.readonly_fields + ('title',)
        return self.readonly_fields

    def get_fieldsets(self, request, obj=None):
        if obj and obj.slug == '/':
            return [(None, { 'fields': ('title', 'body') })]

        return self.declared_fieldsets

    def get_form(self, request, obj=None, **kwargs):
        if obj and obj.slug == '/':
            kwargs['exclude'] = self.readonly + self.hidden
        return super(PageAdmin, self).get_form(request, obj, **kwargs)

class ChunkAdmin(admin.ModelAdmin):
  list_display = ('key', 'content')

class MainPageBlockAdmin(RedactorModelAdmin):
    pass

admin.site.register(Chunk, ChunkAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(MainPageBlock, MainPageBlockAdmin)


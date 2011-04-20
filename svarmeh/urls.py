# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from svarmeh.models import Page, Product
from svarmeh import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view()),
    url(r'^products/$', views.TitledListView.as_view(**{
        'queryset': Product.objects.filter(status='published'),
        'template_name': 'product_list.html',
        'title': u'Продукция',
    }), name='product_list'),
    url(r'^products/(?P<slug>.*)\.html$', views.TitledDetailView.as_view(**{
        'queryset': Product.objects.filter(status='published'),
        'context_object_name': 'product',
        'template_name': 'product_detail.html',
    }), name='product_detail'),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
) + staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )

urlpatterns += patterns('',
    url(r'^(?P<slug>.*)\.html$', views.TitledDetailView.as_view(**{
        'queryset': Page.objects.filter(status='published'),
        'context_object_name': 'page',
        'template_name': 'page_detail.html',
    }), name='page_detail'),
)


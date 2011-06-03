# -*- coding: utf-8 -*-

from django.db.models.signals import post_syncdb
import svarmeh.models

def contacts_chunks(sender, **kwargs):
    for key in (u'Skype', u'Телефон', u'Почта', u'Название сайта'):
        svarmeh.models.Chunk.objects.get_or_create(key=key)

def main_page(sender, **kwargs):
    if not svarmeh.models.Page.objects.filter(slug='/').exists():
        svarmeh.models.Page.objects.create(
                slug='/',
                body='',
                title=u'Главная',
                status='published',
                in_menu=False)


post_syncdb.connect(contacts_chunks, sender=svarmeh.models)
post_syncdb.connect(main_page, sender=svarmeh.models)


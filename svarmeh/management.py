# -*- coding: utf-8 -*-

from django.db.models.signals import post_syncdb
import svarmeh.models

def contacts_chunks(sender, **kwargs):
    for key in (u'Skype', u'Телефон', u'Почта', u'Название сайта'):
        svarmeh.models.Chunk.objects.get_or_create(key=key)

post_syncdb.connect(contacts_chunks, sender=svarmeh.models)


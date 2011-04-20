# -*- coding: utf-8 -*-

from django.db import models
from svarmeh.utils import get_slug
from sorl.thumbnail import ImageField

class Page(models.Model):
    STATUSES = (
        ('draft', u'Черновик'),
        ('published', u'Опубликовано'),
    )

    title = models.CharField(u'Заголовок', max_length=100)
    slug = models.SlugField(u'Ссылка', blank=True, unique=True, help_text=(
        u'Используется в URL. Если оставить пустым - '
        u'автоматически заполняется переводом названия на английский'))
    status = models.CharField(u'Статус', choices=STATUSES, max_length=20, default='draft')
    in_menu = models.BooleanField(u'Отображать в меню', default=True)
    weight = models.IntegerField(u'Вес', default=0,
            help_text=u'Страницы с меньшим весом отображаются в меню первыми')

    body = models.TextField(u'Текст')

    class Meta:
        verbose_name = u'Страница'
        verbose_name_plural = u'Страницы'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('page_detail', (), {'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = self.slug or get_slug(Page, self.title)
        super(Page, self).save(*args, **kwargs)


class Product(models.Model):
    STATUSES = (
        ('draft', u'Черновик'),
        ('published', u'Опубликовано'),
    )

    name = models.CharField(u'Название', max_length=100)
    slug = models.SlugField(u'Ссылка', blank=True, unique=True, help_text=(
        u'Используется в URL. Если оставить пустым - '
        u'автоматически заполняется переводом названия на английский'))
    status = models.CharField(u'Статус', choices=STATUSES, max_length=20, default='draft')
    image = ImageField(u'Картинка', upload_to='products/')

    intro = models.TextField(u'Краткое описание', help_text=u'Показано в списке.')
    description = models.TextField(u'Описание', help_text=u'Показано на странице продукта')

    class Meta:
        verbose_name = u'Продукт'
        verbose_name_plural = u'Продукция'

    @models.permalink
    def get_absolute_url(self):
        return ('product_detail', (), {'slug': self.slug})

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug or get_slug(Product, self.name)
        super(Product, self).save(*args, **kwargs)


class Chunk(models.Model):
    key = models.CharField(u'Ключ', max_length=255, unique=True)
    content = models.TextField(u'Значение', blank=True)

    def __unicode__(self):
        return self.key

    class Meta:
        verbose_name = u'Разное'
        verbose_name_plural = u'Разное'


from django.db import models
from django.db.models import BooleanField
from django.urls import reverse


class AboutUS(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content =models.TextField(blank=True, verbose_name='Котнент')
    photo = models.ImageField(blank=True, verbose_name='Картинка')
    is_published: BooleanField = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация о нас'
        verbose_name_plural = 'Информации о нас'


class Services(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название услуги')
    price = models.IntegerField(blank=True, verbose_name='Цена (руб.)')
    description = models.TextField(blank=True, verbose_name='Краткое описание')
    category = models.ForeignKey('CategoryService', on_delete=models.PROTECT, verbose_name='Категория')
    is_published: BooleanField = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class CategoryService(models.Model):
    title = models.CharField(max_length=30, db_index=True, verbose_name='Заголовок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория услуг'
        verbose_name_plural = 'Категории услуг'
        ordering = ['pk']


class Action(models.Model):
    description = models.TextField(verbose_name='Описание', blank=True)
    photo = models.ImageField(verbose_name='Картинка акции')
    is_published: BooleanField = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
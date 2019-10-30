from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils import timezone
from broadcast.models import *


class GuideStatus(models.Model):
    name = models.CharField(max_length=128, default='Статус', verbose_name='Статус персонала')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата созд-ия записи')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Статус персонала'
        verbose_name_plural = 'Статус персонала'


class Guide(models.Model):
    first_name = models.CharField(max_length=128, blank=True, null=True, default=True, verbose_name='Имя персонала')
    last_name = models.CharField(max_length=128, blank=True, null=True, default=True, verbose_name='Фамилия персонала')
    email = models.EmailField(max_length=128, blank=True, null=True, default=None, verbose_name='Емейл')
    phone = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Номер тел.')
    dob = models.DateField(default=None, null=True, blank=True, verbose_name='Дата рожд-я')
    country = models.CharField(max_length=64, null=True, blank=True, default='Россия', verbose_name='Страна')
    town = models.CharField(max_length=64, blank=True, default='Курск', verbose_name='Город')
    description = models.TextField(max_length=512, null=True, blank=True, default=None,
                                   verbose_name='Описание персонала')
    status = models.ForeignKey(GuideStatus, blank=True, default=True, on_delete=models.CASCADE,
                               verbose_name='Статус персонала')
    vk = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Ссылка VK')
    instagram = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Ссылка instagram')
    twitter = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Ссылка twitter')
    facebook = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Ссылка facebook')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность персонала')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования записи')

    def __str__(self):
        return "%s" % self.last_name

    class Meta:
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководители'


class GuideImage(models.Model):
    guide = models.ForeignKey(Guide, blank=True, null=True, default=None, on_delete=models.CASCADE,
                              verbose_name='Персонал')
    image = models.ImageField(upload_to='guide_images/', verbose_name='Фото')
    is_main = models.BooleanField(default=False, verbose_name='Аватар')
    is_active = models.BooleanField(default=True, verbose_name='Активная?')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата загрузки фото')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия фото')

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография персонала'
        verbose_name_plural = 'Фотографии персоналов'

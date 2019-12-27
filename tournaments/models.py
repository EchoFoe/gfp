from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils import timezone
from broadcast.models import *


class TournamentStatus(models.Model):
    name = models.CharField(max_length=128, default='Статус', verbose_name='Статус турнира')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата созд-ия записи')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Статус турнира'
        verbose_name_plural = 'Статус турнира'


class Tournament(models.Model):
    name = models.TextField(max_length=512,  blank=True, null=True, default=True, verbose_name='Название турнира')
    short_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='Сокращенное название турнира')
    country = models.CharField(max_length=64, null=True, blank=True, default='Россия', verbose_name='Страна')
    region = models.CharField(max_length=64, blank=True, default='Курская область', verbose_name='Регион')
    town = models.CharField(max_length=64, blank=True, default='Курск', verbose_name='Город')
    start_time = models.DateTimeField(null=True, blank=True, default=None, verbose_name='Дата начала турнира')
    end_time = models.DateTimeField(null=True, blank=True, default=None, verbose_name='Дата окончания турнира')
    status = models.ForeignKey(TournamentStatus, blank=True, default=True, on_delete=models.CASCADE,
                               verbose_name='Статус турнира')
    sponsors = models.CharField(max_length=512, null=True, blank=True, default=None, verbose_name='Спонсоры')
    description = models.TextField(max_length=512, null=True, blank=True, default=None, verbose_name='Описание турнира')
    provisions_dk = models.URLField(max_length=1024, blank=True, default=None, null=None,
                                    verbose_name='Положения на турнир с допинг-контролем')
    provisions_bezdk = models.URLField(max_length=1024, blank=True, default=None, null=None,
                                       verbose_name='Положения на турнир без допинг-контроля')
    nominations = models.URLField(max_length=1024, blank=True, default=None, null=None,
                                  verbose_name='Номинации на турнир')
    regulations = models.URLField(max_length=1024, blank=True, default=None, null=True,
                                  verbose_name='Регламент на турнир')
    results = models.URLField(max_length=1024, blank=True, default=None, null=True, verbose_name='Итоги турнира')
    photo_vk = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Ссылка на альбом VK')
    video_youtube = models.URLField(max_length=1024, blank=True, default=None, null=None,
                                    verbose_name='Ссылка на видео YOUTUBE')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность турнира')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания турнира')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования турнира')

    @property
    def Турнир(self):
        return truncatechars(self.name, 64)

    @property
    def Описание(self):
        return truncatechars(self.description, 20)

    def __str__(self):
        return "%s" % self.short_name

    class Meta:
        ordering = ['-start_time']
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'


class TournamentImage(models.Model):
    tournament = models.ForeignKey(Tournament, blank=True, null=True, default=None, on_delete=models.CASCADE,
                                   verbose_name='Турнир')
    image = models.ImageField(upload_to='tournaments_images/', verbose_name='АФиша')
    is_main = models.BooleanField(default=False, verbose_name='Обложка турнира?')
    is_active = models.BooleanField(default=True, verbose_name='Активная?')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата загрузки фото')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия фото')

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография турнира'
        verbose_name_plural = 'Фотографии турниров'


class SportsmanInTournament(models.Model):
    tournament = models.ForeignKey(Tournament, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Турнир')
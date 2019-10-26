from django.db import models
from django.utils import timezone


class Broadcast(models.Model):
    name = models.TextField(max_length=512, blank=True, null=True, default=True, verbose_name='Название трансляции')
    url = models.URLField(max_length=1024, blank=True, default=None, null=None,
                          verbose_name='Ссылка на ТРАНСЛЯЦИЮ с YOUTUBE')
    is_active = models.BooleanField(default=None, verbose_name='Текущая трансляция?')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')

    def __str__(self):
        return "Трансляция соревнований: %s" % self.name

    class Meta:
        verbose_name = 'Трансляция соревнования'
        verbose_name_plural = 'Трансляция соревнований'
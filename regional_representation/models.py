from django.db import models
from django.utils import timezone


class RegionalStatus(models.Model):
    name = models.CharField(max_length=128, default='Статус', verbose_name='Статус представителя ')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность статуса')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата созд-ия записи')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Статус представителя'
        verbose_name_plural = 'Статус представителей'


class Regional(models.Model):
    first_name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Имя')
    last_name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Отчество')
    email = models.EmailField(max_length=128, blank=True, null=True, default=None, verbose_name='Емейл')
    phone = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Номер телефона')
    dob = models.DateField(default=None, null=True, blank=True, verbose_name='Дата рождения')
    status = models.ForeignKey(RegionalStatus, blank=True, default=True, on_delete=models.CASCADE,
                               verbose_name='Статус представителя')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность статуса')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')

    def __str__(self):
        return "Заявка на регионального представителя: %s %s" % (self.last_name, self.first_name)

    class Meta:
        verbose_name = 'Региональный представитель'
        verbose_name_plural = 'Региональные представители'
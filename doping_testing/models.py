from django.db import models
from django.utils import timezone


class Doping(models.Model):
    laboratory = models.TextField(max_length=512, blank=True, null=True, default=True, verbose_name='Название лаборатории')
    illicit_drugs = models.URLField(max_length=1024, blank=True, default=None, null=None,
                                    verbose_name='Список тестируемых препаратов')
    anti_doping_rules = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Антидопинговые правила')
    is_active = models.BooleanField(default=None, verbose_name='Лаборатория лицензированная?')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')

    def __str__(self):
        return "Допинг тестирование: %s" % self.laboratory

    class Meta:
        verbose_name = 'Лаборатория'
        verbose_name_plural = 'Лаборатории'


class AutopsyStatus(models.Model):
    name = models.CharField(max_length=128, default='Статус', verbose_name='Статус пробы Б ')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность статуса')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата созд-ия записи')
    updated = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Статус пробы Б'
        verbose_name_plural = 'Статус пробы Б'


class Autopsy(models.Model):
    first_name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Имя спортсмена')
    last_name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Фамилия спортсмена')
    middle_name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Отчество спортсмена')
    email = models.EmailField(max_length=128, blank=True, null=True, default=None, verbose_name='Емейл')
    phone = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Номер телефона')
    dob = models.DateField(default=None, null=True, blank=True, verbose_name='Дата рождения')
    status = models.ForeignKey(AutopsyStatus, blank=True, default=True, on_delete=models.CASCADE,
                               verbose_name='Статус теста')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность статуса')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')

    def __str__(self):
        return "Заявка на вскрытие пробы 'Б': %s %s" % (self.last_name, self.first_name)

    class Meta:
        verbose_name = 'Вскрытие пробы Б (заявки и результат)'
        verbose_name_plural = 'Вскрытие пробы Б (заявки и результат)'
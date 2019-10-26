from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils import timezone
from tournaments.models import Tournament
from django.db.models.signals import post_save
from utils.main import disable_for_loaddata


class Status(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name="Статус")
    is_active = models.BooleanField(default=True, null=True, blank=True, verbose_name='Активность статуса')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия турнира')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Статус спортсмена'
        verbose_name_plural = 'Статусы спортсменов'


class Gender(models.Model):
    name = models.CharField(max_length=3, blank=True, null=True, default=None, verbose_name="Пол")
    is_active = models.BooleanField(default=True, null=True, blank=True, verbose_name='Активность пола')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия турнира')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Пол спортсмена'
        verbose_name_plural = 'Пол спортсменов'


class Line_up(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name="Команда")
    is_active = models.BooleanField(default=True, null=True, blank=True, verbose_name='Актуальность команды')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия турнира')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Лично/Командно'
        verbose_name_plural = 'Лично/Командно'


class Division(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name="Дивизион")
    is_active = models.BooleanField(default=True, null=True, blank=True, verbose_name='Актуальность')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия турнира')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Дивизион'
        verbose_name_plural = 'Дивизионы'


class Discipline(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name="Дисциплина")
    is_active = models.BooleanField(default=True, null=True, blank=True, verbose_name='Актуальность')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия турнира')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'


class Age_category(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name="Возрастная кат-ия")
    is_active = models.BooleanField(default=True, null=True, blank=True, verbose_name='Актуальность')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия турнира')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Возрастная категория'
        verbose_name_plural = 'Возрастные категории'


class Weight_category(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name="Весовая кат-ия")
    is_active = models.BooleanField(default=True, null=True, blank=True, verbose_name='Актуальность')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия турнира')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Весовая категория'
        verbose_name_plural = 'Весовые категории'


class Sportsman(models.Model):
    first_name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Имя')
    last_name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=64, blank=True, null=True, default=None,
                                   verbose_name='Отчество')
    email = models.EmailField(max_length=128, blank=True, null=True, default=None, verbose_name='Емейл')
    phone = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Номер тел.')
    dob = models.DateField(default=None, null=True, blank=True, verbose_name='Дата рожд-я')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True, blank=True, default=True, verbose_name='Пол')
    weight = models.ForeignKey(Weight_category, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Весовая кат-ия')
    age = models.ForeignKey(Age_category, on_delete=models.CASCADE, null=True, blank=True, default=True, verbose_name='Возраст. кат-ия')
    raised_weight = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, default=00.00,
                                        verbose_name='Поднятый вес (общий)')
    wilkes = models.DecimalField(max_digits=4, decimal_places=2, default=00.00, blank=True, null=True,
                                 verbose_name='КУ')
    country = models.CharField(max_length=64, blank=True, null=True, default='Россия', verbose_name='Страна')
    region = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Регион')
    town = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Город')
    team = models.ForeignKey(Line_up, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Команда/Лично')
    trainer = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Тренер')
    tournament = models.ForeignKey(Tournament, null=True, blank=True, default=True, on_delete=models.CASCADE, verbose_name='Турнир')
    division = models.ForeignKey(Division, blank=True, null=True, default=True, on_delete=models.CASCADE, verbose_name='Дивизион')
    discipline = models.ForeignKey(Discipline, blank=True, null=True, default=True, on_delete=models.CASCADE, verbose_name='Дисциплина')
    status = models.ForeignKey(Status, null=True, blank=True, on_delete=models.CASCADE, default=None, verbose_name='Статус')
    is_active = models.BooleanField(default=False, null=True, blank=True, verbose_name='Явка')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата завяления')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')


    @property
    def Турнир(self):
        return truncatechars(self.tournament, 50)

    @property
    def Дивизион(self):
        return truncatechars(self.division, 32)

    @property
    def Дисциплина(self):
        return truncatechars(self.discipline, 32)

    @property
    def Возрастные_категории(self):
        return truncatechars(self.age, 32)

    def __str__(self):
        return "Спортсмен(ка): %s %s, почта: %s" % (self.first_name, self.last_name, self.email)

    class Meta:
        verbose_name = 'Спортсмен'
        verbose_name_plural = 'Спортсмены'

    def save(self, *args, **kwargs):
        super(Sportsman, self).save(*args, **kwargs)


@disable_for_loaddata
def sportsman_post_save(sender, instance, created, **kwargs):
    pass


post_save.connect(sportsman_post_save, sender=Sportsman)
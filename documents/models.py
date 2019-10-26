from django.db import models
from django.utils import timezone


class Document(models.Model):
    name = models.CharField(max_length=128, default='Документы', verbose_name='Наименование ресурса')
    rules = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Технические правила GFP')
    rules_sfo = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Технические правила GFP СФО')
    standards = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Нормативы')
    sports_regulations = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Положения о присвоении званий GFP')
    norms_sports_titles_dk = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Нормы для присвоения званий GFP (с ДК)')
    norms_sports_titles_bez_dk = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Нормы для присвоения званий GFP (без ДК)')
    tests_secretary = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Тесты для сдачи на секретаря')
    tests_judge = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Тесты для сдачи на судейство')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность документов')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования записи')

    class Meta:
        verbose_name = 'Документ в МЕНЮ'
        verbose_name_plural = 'Документы в МЕНЮ'
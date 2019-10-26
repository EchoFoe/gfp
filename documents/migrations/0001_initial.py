# Generated by Django 2.2.4 on 2019-08-20 15:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Документы', max_length=128, verbose_name='Наименование ресурса')),
                ('rules', models.URLField(blank=True, default=None, max_length=1024, null=None, verbose_name='Технические правила GFP')),
                ('rules_sfo', models.URLField(blank=True, default=None, max_length=1024, null=None, verbose_name='Технические правила GFP СФО')),
                ('standards', models.URLField(blank=True, default=None, max_length=1024, null=None, verbose_name='Нормативы')),
                ('sports_regulations', models.URLField(blank=True, default=None, max_length=1024, null=None, verbose_name='Положения о присвоении званий GFP')),
                ('norms_sports_titles_dk', models.URLField(blank=True, default=None, max_length=1024, null=None, verbose_name='Нормы для присвоения званий GFP (с ДК)')),
                ('norms_sports_titles_bez_dk', models.URLField(blank=True, default=None, max_length=1024, null=None, verbose_name='Нормы для присвоения званий GFP (без ДК)')),
                ('tests_secretary', models.URLField(blank=True, default=None, max_length=1024, null=None, verbose_name='Тесты для сдачи на секретаря')),
                ('tests_judge', models.URLField(blank=True, default=None, max_length=1024, null=None, verbose_name='Тесты для сдачи на судейство')),
                ('is_active', models.BooleanField(default=True, verbose_name='Актуальность документов')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания записи')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата редактирования записи')),
            ],
            options={
                'verbose_name': 'Документ в МЕНЮ',
                'verbose_name_plural': 'Документы в МЕНЮ',
            },
        ),
    ]

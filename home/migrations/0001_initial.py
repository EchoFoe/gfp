# Generated by Django 2.2.4 on 2019-08-15 17:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default=True, max_length=128, verbose_name='Емейл')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата подписки')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата редактирования')),
            ],
            options={
                'verbose_name': 'Подписчик',
                'verbose_name_plural': 'Подписчики',
            },
        ),
    ]

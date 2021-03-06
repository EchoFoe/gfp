# Generated by Django 2.2.4 on 2019-08-17 16:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('broadcast', '0003_auto_20190817_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='broadcast',
            old_name='url',
            new_name='ssilka',
        ),
        migrations.AlterField(
            model_name='broadcast',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания записи'),
        ),
        migrations.AlterField(
            model_name='broadcast',
            name='is_active',
            field=models.BooleanField(default=None, verbose_name='Текущая трансляция?'),
        ),
    ]

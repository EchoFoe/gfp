# Generated by Django 2.2.4 on 2019-12-27 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportsman', '0006_auto_20191219_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsman',
            name='tournament',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sportsman.Tournament', verbose_name='Турнир'),
        ),
    ]

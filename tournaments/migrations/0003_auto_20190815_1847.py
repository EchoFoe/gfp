# Generated by Django 2.2.4 on 2019-08-15 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_auto_20190815_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='photo_vk',
            field=models.URLField(blank=True, default=None, max_length=1024, null=None, verbose_name='Ссылка на альбом VK'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='video_youtube',
            field=models.URLField(blank=True, default=None, max_length=1024, null=None, verbose_name='Ссылка на видео YOUTUBE'),
        ),
    ]

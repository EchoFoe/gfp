# Generated by Django 2.2.4 on 2019-09-22 03:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sportsman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='age_category',
            name='created',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания записи'),
        ),
        migrations.AlterField(
            model_name='age_category',
            name='updated',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата ред-ия турнира'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='created',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания записи'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='updated',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата ред-ия турнира'),
        ),
        migrations.AlterField(
            model_name='division',
            name='created',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания записи'),
        ),
        migrations.AlterField(
            model_name='division',
            name='updated',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата ред-ия турнира'),
        ),
        migrations.AlterField(
            model_name='gender',
            name='created',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания записи'),
        ),
        migrations.AlterField(
            model_name='gender',
            name='updated',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата ред-ия турнира'),
        ),
        migrations.AlterField(
            model_name='line_up',
            name='created',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания записи'),
        ),
        migrations.AlterField(
            model_name='line_up',
            name='updated',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата ред-ия турнира'),
        ),
        migrations.AlterField(
            model_name='sportsman',
            name='age',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sportsman.Age_category', verbose_name='Возраст. кат-ия'),
        ),
        migrations.AlterField(
            model_name='sportsman',
            name='created',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата завяления'),
        ),
        migrations.AlterField(
            model_name='sportsman',
            name='division',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sportsman.Division', verbose_name='Дивизион'),
        ),
        migrations.AlterField(
            model_name='sportsman',
            name='gender',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sportsman.Gender', verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='sportsman',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Явка'),
        ),
        migrations.AlterField(
            model_name='sportsman',
            name='status',
            field=models.ForeignKey(blank=True, default=1861006496, null=True, on_delete=django.db.models.deletion.CASCADE, to='sportsman.Status', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='sportsman',
            name='tournament',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament', verbose_name='Турнир'),
        ),
        migrations.AlterField(
            model_name='sportsman',
            name='updated',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата ред-ия записи'),
        ),
        migrations.AlterField(
            model_name='status',
            name='created',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания записи'),
        ),
        migrations.AlterField(
            model_name='status',
            name='updated',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата ред-ия турнира'),
        ),
        migrations.AlterField(
            model_name='weight_category',
            name='created',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания записи'),
        ),
        migrations.AlterField(
            model_name='weight_category',
            name='updated',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата ред-ия турнира'),
        ),
    ]

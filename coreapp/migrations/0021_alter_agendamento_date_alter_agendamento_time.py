# Generated by Django 5.0 on 2024-02-22 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0020_alter_agendamento_date_alter_agendamento_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='date',
            field=models.CharField(max_length=15, verbose_name='horário'),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='time',
            field=models.TimeField(),
        ),
    ]

# Generated by Django 5.0 on 2024-02-19 01:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0019_alter_aluno_grupo_de_atendimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='date',
            field=models.DateField(verbose_name='horário'),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='time',
            field=models.TimeField(choices=[('13:00', datetime.time(13, 0)), ('14:00', datetime.time(14, 0)), ('15:00', datetime.time(15, 0)), ('16:00', datetime.time(16, 0)), ('17:00', datetime.time(17, 0))]),
        ),
    ]
# Generated by Django 5.0 on 2024-03-02 20:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0027_remove_aluno_agendamentos'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='aluno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='coreapp.aluno'),
        ),
    ]

# Generated by Django 5.0 on 2024-03-02 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0026_aluno_agendamentos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='agendamentos',
        ),
    ]
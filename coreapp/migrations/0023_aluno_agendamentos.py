# Generated by Django 5.0 on 2024-03-02 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0022_remove_agendamento_time_alter_agendamento_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='agendamentos',
            field=models.ManyToManyField(blank=True, to='coreapp.agendamento'),
        ),
    ]

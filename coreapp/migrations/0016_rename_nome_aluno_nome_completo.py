# Generated by Django 5.0 on 2024-01-06 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0015_alter_aluno_grupo_de_atendimento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='nome',
            new_name='nome_completo',
        ),
    ]

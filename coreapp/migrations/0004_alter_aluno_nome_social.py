# Generated by Django 5.0 on 2023-12-28 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0003_alter_aluno_nome_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='nome_social',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]

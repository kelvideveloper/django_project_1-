# Generated by Django 5.0 on 2023-12-27 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]

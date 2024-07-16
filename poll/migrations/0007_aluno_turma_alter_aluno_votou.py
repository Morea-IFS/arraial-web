# Generated by Django 5.0.6 on 2024-07-16 23:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0006_rename_numero_candidata_candidata_numero_da_candidata_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='turma',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='votou',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
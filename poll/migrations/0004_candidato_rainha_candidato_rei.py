# Generated by Django 5.0.6 on 2024-07-15 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_delete_voto_alter_candidato_votos_candidato'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='rainha',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='candidato',
            name='rei',
            field=models.BooleanField(default=False),
        ),
    ]

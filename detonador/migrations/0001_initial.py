# Generated by Django 5.0.6 on 2024-07-03 01:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_device'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detonador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.IntegerField(choices=[(0, 'Not Selected'), (1, 'D1'), (2, 'D2'), (3, 'D3'), (4, 'D4'), (5, 'D5'), (6, 'D6'), (7, 'D7'), (8, 'D8')], default=0)),
                ('status', models.BooleanField(default=False)),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.device')),
            ],
        ),
    ]

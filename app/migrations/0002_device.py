# Generated by Django 5.0.6 on 2024-07-02 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('application', models.IntegerField(choices=[(0, 'Not Defined'), (1, 'Vestido'), (2, 'Detonador'), (3, 'Displays')], default=0)),
                ('is_authorized', models.IntegerField(choices=[(0, 'Pending'), (1, 'Not Authorized'), (2, 'Authorized')], default=0)),
                ('mac_address', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('api_token', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
        ),
    ]

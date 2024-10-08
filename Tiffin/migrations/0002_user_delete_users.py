# Generated by Django 5.0 on 2024-02-29 10:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tiffin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('iduser', models.AutoField(primary_key=True, serialize=False)),
                ('Your_name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45, unique=True)),
                ('password', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=True)),
                ('otp', models.IntegerField(default=0)),
                ('otp_expiry', models.DateTimeField(blank=True, null=True)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('profile_image', models.FileField(blank=True, default=None, max_length=250, null=True, upload_to='users_profils/')),
            ],
        ),
        migrations.DeleteModel(
            name='users',
        ),
    ]

# Generated by Django 5.0 on 2024-06-02 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tiffin', '0005_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('day_id', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.PositiveSmallIntegerField()),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tiffin.month')),
            ],
            options={
                'db_table': 'Day',
                'managed': True,
            },
        ),
    ]

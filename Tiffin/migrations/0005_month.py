# Generated by Django 5.0 on 2024-06-02 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tiffin', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('month_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Month',
                'managed': True,
            },
        ),
    ]

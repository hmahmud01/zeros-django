# Generated by Django 3.0.3 on 2020-03-30 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_clients'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

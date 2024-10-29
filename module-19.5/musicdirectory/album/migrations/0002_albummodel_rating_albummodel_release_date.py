# Generated by Django 5.1.1 on 2024-10-29 04:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='albummodel',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='albummodel',
            name='release_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
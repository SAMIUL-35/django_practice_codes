# Generated by Django 5.1.1 on 2024-11-29 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbankaccount',
            name='is_bankrupt',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 4.2.3 on 2024-02-01 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finance',
            name='user',
        ),
    ]
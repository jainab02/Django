# Generated by Django 4.2.3 on 2024-02-05 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='totalAmt',
        ),
    ]

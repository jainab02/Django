# Generated by Django 5.0.1 on 2024-01-29 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('state', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('profimage', models.ImageField(blank=True, upload_to='resumeImages')),
                ('resumeDoc', models.FileField(blank=True, upload_to='resumeDocs')),
            ],
        ),
    ]
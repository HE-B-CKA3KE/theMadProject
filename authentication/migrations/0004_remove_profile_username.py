# Generated by Django 4.0.6 on 2022-09-16 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_profile_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]

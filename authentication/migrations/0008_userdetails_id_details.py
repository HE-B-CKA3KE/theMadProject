# Generated by Django 4.0.6 on 2022-10-20 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_userdetails_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='id_details',
            field=models.IntegerField(default=0),
        ),
    ]

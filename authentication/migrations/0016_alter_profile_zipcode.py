# Generated by Django 4.0.6 on 2022-10-21 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_delete_userdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

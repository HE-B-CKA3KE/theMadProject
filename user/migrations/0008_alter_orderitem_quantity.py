# Generated by Django 4.0.6 on 2022-10-30 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_delete_usercart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
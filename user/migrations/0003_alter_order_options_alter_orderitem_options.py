# Generated by Django 4.0.6 on 2022-10-13 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_usercart_alter_order_customer_orderitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Order'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name_plural': 'OrderItem'},
        ),
    ]

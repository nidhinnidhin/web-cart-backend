# Generated by Django 4.1 on 2023-05-20 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_alter_cart_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='address',
        ),
    ]
# Generated by Django 4.0 on 2022-08-01 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
    ]

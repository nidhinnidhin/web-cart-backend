# Generated by Django 4.1.1 on 2022-10-28 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_wishlist_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='liked',
        ),
    ]

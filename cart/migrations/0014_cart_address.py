# Generated by Django 4.1 on 2023-05-27 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('cart', '0013_remove_cart_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='address',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='address.address'),
        ),
    ]

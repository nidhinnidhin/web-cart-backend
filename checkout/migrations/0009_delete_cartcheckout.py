# Generated by Django 4.0 on 2022-09-28 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_alter_cartcheckout_checked_out_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartCheckout',
        ),
    ]
# Generated by Django 4.0 on 2022-09-27 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_cartcheckout_checked_out_alter_cartcheckout_payed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartcheckout',
            name='checked_out',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='cartcheckout',
            name='payed',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
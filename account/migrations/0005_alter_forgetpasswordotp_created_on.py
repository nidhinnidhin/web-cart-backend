# Generated by Django 4.1.1 on 2022-12-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_forgetpasswordotp_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forgetpasswordotp',
            name='created_on',
            field=models.DateTimeField(),
        ),
    ]

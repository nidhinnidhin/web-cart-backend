# Generated by Django 4.0 on 2022-09-16 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('checkout', '0005_alter_cartcheckout_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartcheckout',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='auth.user'),
        ),
    ]
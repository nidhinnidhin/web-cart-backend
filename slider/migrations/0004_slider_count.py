# Generated by Django 4.0 on 2022-08-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0003_slider_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='count',
            field=models.IntegerField(default=1, null=True),
        ),
    ]

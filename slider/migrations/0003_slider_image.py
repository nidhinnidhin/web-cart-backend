# Generated by Django 4.0 on 2022-07-29 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0002_remove_slider_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

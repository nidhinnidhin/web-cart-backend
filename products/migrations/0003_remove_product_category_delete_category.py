# Generated by Django 4.0 on 2022-07-22 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]

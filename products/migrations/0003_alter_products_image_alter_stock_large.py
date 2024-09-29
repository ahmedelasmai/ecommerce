# Generated by Django 5.0.3 on 2024-09-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_options_remove_products_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='products/static/products/images/products'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='large',
            field=models.IntegerField(),
        ),
    ]
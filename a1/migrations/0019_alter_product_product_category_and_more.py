# Generated by Django 4.2.3 on 2023-08-01 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0018_alter_product_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(choices=[('Laptop', 'Laptop'), ('accessories', 'Accessories'), ('Electronics', 'Electronics'), ('Men', 'Men'), ('Women', 'Women'), ('Baby & Kids', 'Baby & Kids'), ('Home & Kitchens', 'Home & Kitchens'), ('Books', 'Books'), ('Other', 'Other')], default='Others', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=models.CharField(max_length=300),
        ),
    ]

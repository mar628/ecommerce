# Generated by Django 4.2.3 on 2023-08-20 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0023_alter_product_product_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(choices=[('Laptop', 'Laptop'), ('Accessories', 'Accessories'), ('Iron', 'Iron'), ('Electronics', 'Electronics'), ('Men', 'Men'), ('Formal', 'Formal'), ('Women', 'Women'), ('Baby & Kids', 'Baby & Kids'), ('Home & Kitchens', 'Home & Kitchens'), ('Books', 'Books'), ('Other', 'Other')], default='Others', max_length=50),
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-01 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0019_alter_product_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(choices=[('Laptop', 'Laptop'), ('Accessories', 'Accessories'), ('Iron', 'Iron'), ('Electronics', 'Electronics'), ('Men', 'Men'), ('Women', 'Women'), ('Baby & Kids', 'Baby & Kids'), ('Home & Kitchens', 'Home & Kitchens'), ('Books', 'Books'), ('Other', 'Other')], default='Others', max_length=50),
        ),
    ]

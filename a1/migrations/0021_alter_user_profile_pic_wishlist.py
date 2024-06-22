# Generated by Django 4.2.3 on 2023-08-09 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0020_alter_product_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='usericon.jpg', upload_to='profile_pic/'),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a1.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a1.user')),
            ],
        ),
    ]
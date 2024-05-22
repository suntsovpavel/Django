# Generated by Django 5.0.6 on 2024-05-22 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='imageName',
            field=models.CharField(default='default_image.png', max_length=100),
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-22 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_order_date_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FilePathField(default='/media/default_image.png'),
        ),
    ]

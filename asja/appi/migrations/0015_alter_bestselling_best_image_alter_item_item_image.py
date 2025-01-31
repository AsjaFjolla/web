# Generated by Django 5.1.4 on 2025-01-28 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appi', '0014_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestselling',
            name='best_image',
            field=models.ImageField(blank=True, null=True, upload_to='item/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(blank=True, null=True, upload_to='journal/'),
        ),
    ]

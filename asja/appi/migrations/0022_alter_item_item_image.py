# Generated by Django 5.1.4 on 2025-02-04 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appi', '0021_book_book_jornual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(blank=True, null=True, upload_to='best/'),
        ),
    ]

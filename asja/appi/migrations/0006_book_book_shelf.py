# Generated by Django 5.1.4 on 2025-01-22 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appi', '0005_remove_category_category_image_book_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_shelf',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]

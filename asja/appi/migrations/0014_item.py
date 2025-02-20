# Generated by Django 5.1.4 on 2025-01-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appi', '0013_delete_journal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(blank=True, max_length=250, null=True)),
                ('item_image', models.ImageField(blank=True, null=True, upload_to='item/')),
                ('item_description', models.TextField(blank=True, max_length=500, null=True)),
                ('item_price', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
            ],
        ),
    ]

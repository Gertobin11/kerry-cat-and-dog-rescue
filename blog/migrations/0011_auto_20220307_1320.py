# Generated by Django 3.2 on 2022-03-07 13:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rename_featured_image_post_placeholder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='placeholder',
        ),
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
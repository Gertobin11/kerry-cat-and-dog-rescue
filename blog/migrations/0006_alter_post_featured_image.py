# Generated by Django 3.2 on 2022-03-02 14:44

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='http://placekitten.com/200/300', max_length=255, verbose_name='image'),
        ),
    ]

# Generated by Django 3.2 on 2022-03-02 14:50

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='https://codeinstitute.s3.amazonaws.com/fullstack/blog/default.jpg', max_length=255, verbose_name='image'),
        ),
    ]

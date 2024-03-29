# Generated by Django 3.2 on 2022-03-30 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dogs', '0002_dogadoption_applied_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogadoption',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dogadoption',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 3.0.3 on 2020-11-23 19:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20201123_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumdescription',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
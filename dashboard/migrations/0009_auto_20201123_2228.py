# Generated by Django 3.0.3 on 2020-11-23 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commonops', '0006_auto_20201123_0231'),
        ('dashboard', '0008_albumdescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumdescription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commonops.User', verbose_name='Owner'),
        ),
    ]
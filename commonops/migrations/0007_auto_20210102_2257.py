# Generated by Django 3.1.4 on 2021-01-02 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commonops', '0006_auto_20201123_0231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='middle_name',
        ),
    ]
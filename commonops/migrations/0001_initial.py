# Generated by Django 3.0.3 on 2020-07-14 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'users',
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('upload_date', models.DateTimeField()),
                ('video', models.FileField(upload_to='uploads/videos')),
                ('collection', models.ManyToManyField(to='commonops.Collection')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commonops.User', verbose_name='Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateTimeField()),
                ('picture', models.ImageField(upload_to='uploads/pictures')),
                ('collection', models.ManyToManyField(to='commonops.Collection')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commonops.User', verbose_name='Owner')),
            ],
        ),
    ]

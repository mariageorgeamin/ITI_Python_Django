# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-21 21:53
from __future__ import unicode_literals

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.IntegerField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=100)),
                ('city_title', models.CharField(max_length=200)),
                ('city_desc', models.CharField(max_length=500)),
                ('city_img', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/elmansy/ITI_Python_Django/Django_lonelyplanet/home_site/static/'), upload_to='')),
                ('city_rate', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_description', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_site.City')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.IntegerField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=100)),
                ('country_title', models.CharField(max_length=200)),
                ('country_desc', models.CharField(max_length=500)),
                ('country_img', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/elmansy/ITI_Python_Django/Django_lonelyplanet/home_site/static/'), upload_to='')),
                ('country_rate', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('exp_id', models.AutoField(primary_key=True, serialize=False)),
                ('exp_title', models.CharField(max_length=200)),
                ('exp_description', models.CharField(max_length=250)),
                ('exp_img', models.ImageField(default='default.jpeg', upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_site.City')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('hotel_id', models.AutoField(primary_key=True, serialize=False)),
                ('hotel_name', models.CharField(max_length=200)),
                ('hotel_img', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/elmansy/ITI_Python_Django/Django_lonelyplanet/home_site/static/'), upload_to='')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_site.City')),
            ],
        ),
        migrations.CreateModel(
            name='Sights',
            fields=[
                ('sight_id', models.AutoField(primary_key=True, serialize=False)),
                ('sight_name', models.CharField(max_length=200)),
                ('sight_img', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/elmansy/ITI_Python_Django/Django_lonelyplanet/home_site/static/'), upload_to='')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_site.City')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='exp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_site.Experience'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='count', to='home_site.Country'),
        ),
    ]

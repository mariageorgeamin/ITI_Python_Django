# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-20 16:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home_site', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_date', models.DateField(verbose_name='Date')),
                ('from_time', models.TimeField(verbose_name='Time')),
                ('to_date', models.DateField(verbose_name='Date')),
                ('to_time', models.TimeField(verbose_name='Time')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_destination', to='home_site.Sights')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_site.Sights')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('hotel_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_date', models.DateField(verbose_name='Date')),
                ('to_date', models.DateField(verbose_name='Date')),
                ('person_number', models.IntegerField(default='1')),
                ('hotels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_site.Hotels')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 05:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0015_auto_20160421_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmartMirrorWeatherPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('zip_code', models.CharField(default='20500', max_length=5, verbose_name='zip code (5-digit)')),
                ('api_key', models.CharField(default='', max_length=32, verbose_name='WUnderground API key')),
                ('alignment', models.CharField(choices=[('left', 'left'), ('right', 'right')], default='left', max_length=5, verbose_name='Text alignment')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
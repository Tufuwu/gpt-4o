# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-02 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0017_auto_20161225_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='mailchimp_api_key',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='mailchimp_list_id',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='mailchimp_username',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]

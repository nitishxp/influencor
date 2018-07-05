# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-05 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180705_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='bank_acc_no',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='bank_ifsc_code',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='bank_name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='no_of_followers',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='physical_shows',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='social_media',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='social_media_url',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='stage_show_name',
            field=models.TextField(null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-18 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_userprofile_user_img_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_bio',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedsappsettings',
            name='feed_author_email',
            field=models.EmailField(blank=True, help_text=b'Email of author', max_length=255),
        ),
        migrations.AddField(
            model_name='feedsappsettings',
            name='feed_author_link',
            field=models.URLField(blank=True, help_text=b'Link of author', max_length=255),
        ),
        migrations.AddField(
            model_name='feedsappsettings',
            name='feed_description',
            field=models.CharField(blank=True, help_text=b'Description of field', max_length=255),
        ),
        migrations.AddField(
            model_name='feedsappsettings',
            name='feed_item_content_field',
            field=models.CharField(blank=True, help_text=b'Content Field for feed item', max_length=255),
        ),
        migrations.AddField(
            model_name='feedsappsettings',
            name='feed_item_description_field',
            field=models.CharField(blank=True, help_text=b'Description field for feed item', max_length=255),
        ),
        migrations.AddField(
            model_name='feedsappsettings',
            name='feed_link',
            field=models.URLField(blank=True, help_text=b'link for Feed', max_length=255),
        ),
        migrations.AddField(
            model_name='feedsappsettings',
            name='feed_title',
            field=models.CharField(blank=True, help_text=b'Title of Feed', max_length=255),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='batch',
            field=models.CharField(default=b'Btech2014', max_length=9),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='fname',
            field=models.CharField(default=b' ', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='lname',
            field=models.CharField(default=b' ', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='rollno',
            field=models.IntegerField(max_length=7),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='stream',
            field=models.CharField(default=b'ECE', max_length=3),
            preserve_default=True,
        ),
    ]

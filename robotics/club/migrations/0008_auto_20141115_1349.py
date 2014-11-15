# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0007_projects_mem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='rollno',
            field=models.IntegerField(default=b'1', max_length=7),
            preserve_default=True,
        ),
    ]

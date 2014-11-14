# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20141114_1209'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='members',
        ),
    ]

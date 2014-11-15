# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0010_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anouncement',
            name='description',
        ),
    ]

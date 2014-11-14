# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0006_interests_projects_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='mem',
            field=models.ForeignKey(blank=True, to='club.members', null=True),
            preserve_default=True,
        ),
    ]

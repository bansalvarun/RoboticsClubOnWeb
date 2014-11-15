# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0008_auto_20141115_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='anouncement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('author', models.ForeignKey(blank=True, to='club.members', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

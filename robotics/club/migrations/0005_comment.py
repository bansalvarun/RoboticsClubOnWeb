# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=50)),
                ('author', models.ForeignKey(blank=True, to='club.members', null=True)),
                ('discussion', models.ForeignKey(blank=True, to='club.post', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('stream', models.CharField(max_length=3)),
                ('role', models.IntegerField(max_length=1)),
                ('batch', models.CharField(max_length=9)),
                ('rollno', models.BigIntegerField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

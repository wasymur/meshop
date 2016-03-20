# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('ID', models.AutoField(serialize=False, primary_key=True)),
                ('CreateDate', models.DateTimeField(auto_now_add=True)),
                ('UpdateDate', models.DateTimeField(auto_now=True, null=True)),
                ('DeleteDate', models.DateTimeField(null=True, blank=True)),
                ('Deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=10000, null=True, blank=True)),
                ('active', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('site', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

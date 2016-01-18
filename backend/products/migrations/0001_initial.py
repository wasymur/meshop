# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ID', models.AutoField(serialize=False, primary_key=True)),
                ('CreateDate', models.DateTimeField(auto_now_add=True)),
                ('UpdateDate', models.DateTimeField(auto_now=True, null=True)),
                ('DeleteDate', models.DateTimeField(null=True, blank=True)),
                ('Deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=300, null=True, blank=True)),
                ('about', models.CharField(max_length=10000, null=True, blank=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ID', models.AutoField(serialize=False, primary_key=True)),
                ('CreateDate', models.DateTimeField(auto_now_add=True)),
                ('UpdateDate', models.DateTimeField(auto_now=True, null=True)),
                ('DeleteDate', models.DateTimeField(null=True, blank=True)),
                ('Deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=300, null=True, blank=True)),
                ('about', models.CharField(max_length=10000)),
                ('price', models.PositiveSmallIntegerField(default=0)),
                ('video', models.CharField(max_length=1000, null=True, blank=True)),
                ('status', models.CharField(default=b'waiting', max_length=30, db_index=True, choices=[(b'waiting', b'Waiting'), (b'new', b'New'), (b'approved', b'Approved'), (b'closed', b'Closed'), (b'canceled', b'Canceled')])),
                ('active', models.BooleanField(default=False)),
                ('category', models.ForeignKey(to='products.Category', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

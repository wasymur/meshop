# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0001_initial'),
        ('products', '0003_auto_20160120_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='provider',
            field=models.ForeignKey(to='providers.Provider', null=True),
        ),
    ]

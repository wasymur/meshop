# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20160208_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='about',
            field=models.TextField(max_length=10000),
        ),
    ]

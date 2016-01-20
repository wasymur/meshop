# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_customer_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='expiration_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(default=b'waiting', max_length=30, db_index=True, choices=[(b'waiting', b'Waiting'), (b'approved', b'Approved'), (b'closed', b'Closed')]),
        ),
    ]

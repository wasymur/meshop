# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='customer_price',
            new_name='provider_price',
        ),
    ]

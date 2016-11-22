# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0012_cart_subtotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='subtotal',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(to='carts.Cart'),
        ),
    ]

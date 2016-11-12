# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0003_utwor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='published_date',
        ),
        migrations.AddField(
            model_name='utwor',
            name='IloscWyswietlen',
            field=models.DecimalField(default=Decimal('0'), decimal_places=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='utwor',
            name='imgurl',
            field=models.CharField(default='kappa', max_length=200),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Utwor', '0002_auto_20161111_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utwor',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]

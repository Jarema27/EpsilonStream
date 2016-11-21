# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0004_auto_20161112_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utwor',
            name='text',
        ),
        migrations.AddField(
            model_name='utwor',
            name='song',
            field=models.FileField(null=True, upload_to=b'music'),
        ),
    ]

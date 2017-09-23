# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicineMain', '0008_scrollimage_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='xcxuser',
            name='xcxCode',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]

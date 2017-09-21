# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicineMain', '0007_auto_20170904_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrollimage',
            name='url',
            field=models.URLField(verbose_name='\u8df3\u8f6c\u5730\u5740', blank=True),
        ),
    ]

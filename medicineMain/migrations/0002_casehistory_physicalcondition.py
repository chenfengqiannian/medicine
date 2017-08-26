# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicineMain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casehistory',
            name='physicalCondition',
            field=models.CharField(max_length=255, verbose_name='\u8eab\u4f53\u72b6\u51b5', blank=True),
        ),
    ]

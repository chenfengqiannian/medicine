# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicineMain', '0006_casehistory_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casehistory',
            name='body',
        ),
        migrations.AddField(
            model_name='xcxuser',
            name='body',
            field=models.IntegerField(default=0, verbose_name='\u8eab\u4f53\u72b6\u51b5', choices=[(-1, '\u80c3\u5bd2'), (0, '\u80c3\u4e2d\u6027'), (1, '\u80c3\u70ed')]),
        ),
    ]

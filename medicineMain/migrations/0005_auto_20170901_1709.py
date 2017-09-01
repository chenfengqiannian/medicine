# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicineMain', '0004_auto_20170901_1607'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': '\u5730\u5740\u4fe1\u606f', 'verbose_name_plural': '\u5730\u5740\u4fe1\u606f'},
        ),
        migrations.AlterModelOptions(
            name='casehistory',
            options={'verbose_name': '\u75c5\u4f8b\u7ba1\u7406', 'verbose_name_plural': '\u75c5\u4f8b\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='indeximage',
            options={'verbose_name': '\u9996\u9875\u56fe\u7247', 'verbose_name_plural': '\u9996\u9875\u56fe\u7247'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': '\u7cfb\u7edf\u6d88\u606f', 'verbose_name_plural': '\u7cfb\u7edf\u6d88\u606f'},
        ),
        migrations.AlterModelOptions(
            name='scrollimage',
            options={'verbose_name': '\u6eda\u52a8\u56fe\u7247', 'verbose_name_plural': '\u6eda\u52a8\u56fe\u7247'},
        ),
        migrations.AlterModelOptions(
            name='symptom',
            options={'verbose_name': '\u75c7\u72b6\u7ba1\u7406', 'verbose_name_plural': '\u75c7\u72b6\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='userimage',
            options={'verbose_name': '\u7528\u6237\u56fe\u7247', 'verbose_name_plural': '\u7528\u6237\u56fe\u7247'},
        ),
        migrations.AlterModelOptions(
            name='xcxuser',
            options={'verbose_name': '\u7528\u6237\u7ba1\u7406', 'verbose_name_plural': '\u7528\u6237\u7ba1\u7406'},
        ),
        migrations.AddField(
            model_name='xcxuser',
            name='code',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]

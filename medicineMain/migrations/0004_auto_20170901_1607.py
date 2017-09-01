# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicineMain', '0003_auto_20170826_0641'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'images', max_length=255, verbose_name='\u56fe\u7247')),
            ],
        ),
        migrations.AddField(
            model_name='scrollimage',
            name='imageDetail',
            field=models.ImageField(upload_to=b'images', max_length=255, verbose_name='\u5185\u90e8\u8be6\u60c5', blank=True),
        ),
    ]

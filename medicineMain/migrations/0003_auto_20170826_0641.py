# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicineMain', '0002_casehistory_physicalcondition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='caseHistotyForeign',
            field=models.ForeignKey(blank=True, to='medicineMain.CaseHistory', null=True),
        ),
    ]

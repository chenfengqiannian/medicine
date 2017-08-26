# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u59d3\u540d')),
                ('detailAddress', models.CharField(max_length=255, verbose_name='\u5730\u5740', blank=True)),
                ('contact', models.CharField(max_length=255, verbose_name='\u7535\u8bdd', blank=True)),
                ('province', models.CharField(max_length=255, verbose_name='\u7701', blank=True)),
                ('city', models.CharField(max_length=255, verbose_name='\u5e02', blank=True)),
                ('district', models.CharField(max_length=255, verbose_name='\u533a', blank=True)),
                ('countyName', models.CharField(max_length=255, verbose_name='\u56fd', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CaseHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u59d3\u540d', blank=True)),
                ('tel', models.CharField(max_length=255, verbose_name='\u8054\u7cfb\u7535\u8bdd', blank=True)),
                ('height', models.CharField(max_length=255, verbose_name='\u8eab\u9ad8', blank=True)),
                ('weight', models.CharField(max_length=255, verbose_name='\u4f53\u91cd', blank=True)),
                ('birthday', models.DateField(null=True, verbose_name='\u751f\u65e5', blank=True)),
                ('figure', models.CharField(max_length=255, verbose_name='\u4f53\u5f62', blank=True)),
                ('sex', models.CharField(max_length=255, verbose_name='\u6027\u522b', blank=True)),
                ('allergyHistory', models.TextField(verbose_name='\u8fc7\u654f\u53f2', blank=True)),
                ('medicalHistory', models.TextField(verbose_name='\u8fc7\u53bb\u7684\u8fc7\u4ec0\u4e48\u75c5', blank=True)),
                ('modDateTime', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65e5\u671f')),
                ('createDateTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65e5\u671f')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(max_length=255, verbose_name='\u6d88\u606f')),
                ('modDateTime', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65e5\u671f')),
                ('createDateTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65e5\u671f')),
            ],
        ),
        migrations.CreateModel(
            name='ScrollImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'images', max_length=255, verbose_name='\u56fe\u7247')),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symptomName', models.CharField(max_length=255, verbose_name='\u75c7\u72b6\u540d')),
                ('sick', models.IntegerField(default=0, verbose_name='\u75c5\u75c7', choices=[(-1, '\u80c3\u5bd2'), (1, '\u80c3\u70ed')])),
                ('CaseHistoryForeign', models.ManyToManyField(to='medicineMain.CaseHistory', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'images', max_length=255, verbose_name='\u56fe\u7247')),
                ('caseHistotyForeign', models.ForeignKey(to='medicineMain.CaseHistory')),
            ],
        ),
        migrations.CreateModel(
            name='XcxUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('openid', models.CharField(max_length=255)),
                ('session', models.CharField(max_length=255, blank=True)),
                ('xcxSession', models.CharField(max_length=255, blank=True)),
                ('modDateTime', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65e5\u671f')),
                ('createDateTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65e5\u671f')),
                ('phone', models.CharField(max_length=255, verbose_name='\u624b\u673a', blank=True)),
                ('passWord', models.CharField(max_length=255, verbose_name='\u5bc6\u7801', blank=True)),
                ('gender', models.CharField(max_length=255, blank=True)),
                ('city', models.CharField(max_length=255, blank=True)),
                ('province', models.CharField(max_length=255, blank=True)),
                ('country', models.CharField(max_length=255, blank=True)),
                ('avatarUrl', models.CharField(max_length=255, blank=True)),
                ('nickname', models.CharField(max_length=255, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='casehistory',
            name='xcxUserForeign',
            field=models.ForeignKey(to='medicineMain.XcxUser'),
        ),
        migrations.AddField(
            model_name='address',
            name='xcxUserForeign',
            field=models.ForeignKey(to='medicineMain.XcxUser'),
        ),
    ]

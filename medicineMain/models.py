#coding=utf-8
from django.db import models
# Create your models here.
class XcxUser(models.Model):
    openid = models.CharField(max_length=255)
    session = models.CharField(max_length=255, blank=True)
    xcxCode=models.CharField(max_length=255, blank=True)
    xcxSession = models.CharField(max_length=255, blank=True)
    modDateTime = models.DateTimeField(u'最后修改日期', auto_now=True)
    createDateTime = models.DateTimeField(u'创建日期', auto_now_add=True)
    phone = models.CharField(u"手机", max_length=255, blank=True)
    passWord = models.CharField(u"密码", max_length=255, blank=True)
    gender = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    province = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    avatarUrl = models.CharField(max_length=255, blank=True)
    nickname = models.CharField(max_length=255, blank=True)
    code=models.CharField(max_length=255,blank=True)
    bodyChoices = ((-1, u'胃寒'), (0, u"胃中性"), (1, u'胃热'))
    body = models.IntegerField(u'身体状况', choices=bodyChoices, default=0)

    def __unicode__(self):
        return self.nickname
    class Meta:
        verbose_name=u"用户管理"
        verbose_name_plural=u"用户管理"
class CaseHistory(models.Model):
    xcxUserForeign=models.ForeignKey(XcxUser)
    name=models.CharField(u"姓名",max_length=255,blank=True)
    tel = models.CharField(u"联系电话", max_length=255, blank=True)
    height = models.CharField(u"身高", max_length=255, blank=True)
    weight = models.CharField(u"体重", max_length=255, blank=True)
    birthday = models.DateField(u'生日',blank=True,null=True)
    figure = models.CharField(u"体形", max_length=255, blank=True)
    sex=models.CharField(u'性别',max_length=255,blank=True)
    allergyHistory= models.TextField(u"过敏史",blank=True)
    medicalHistory = models.TextField(u'过去的过什么病',blank=True)
    modDateTime = models.DateTimeField(u'最后修改日期', auto_now=True)
    createDateTime = models.DateTimeField(u'创建日期', auto_now_add=True)
    physicalCondition=models.CharField(u"身体状况", max_length=255, blank=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name=u"病例管理"
        verbose_name_plural=u"病例管理"
class Symptom(models.Model):
    CaseHistoryForeign=models.ManyToManyField(CaseHistory,blank=True)
    symptomName=models.CharField(u"症状名",max_length=255)
    sickChoices = ((-1, u'胃寒'), (1, u'胃热'))
    sick=models.IntegerField(u'病症',choices=sickChoices,default=0)
    def __unicode__(self):
        return self.symptomName
    class Meta:
        verbose_name=u"症状管理"
        verbose_name_plural=u"症状管理"

class UserImage(models.Model):
    caseHistotyForeign=models.ForeignKey(CaseHistory,blank=True,null=True)
    image=models.ImageField(u'图片',upload_to='images', max_length=255)
    class Meta:
        verbose_name=u"用户图片"
        verbose_name_plural=u"用户图片"
class ScrollImage(models.Model):
    image=models.ImageField(u"图片",upload_to="images",max_length=255)
    imageDetail=models.ImageField(u"内部详情",upload_to="images",max_length=255,blank=True)
    url=models.URLField(u"跳转地址",blank=True)
    class Meta:
        verbose_name=u"滚动图片"
        verbose_name_plural=u"滚动图片"

class IndexImage(models.Model):
    image=models.ImageField(u"图片",upload_to="images",max_length=255)
    class Meta:
        verbose_name=u"首页图片"
        verbose_name_plural=u"首页图片"

class Message(models.Model):
    text=models.TextField(u"消息",max_length=255)
    modDateTime = models.DateTimeField(u'最后修改日期', auto_now=True)
    createDateTime = models.DateTimeField(u'创建日期', auto_now_add=True)
    class Meta:
        verbose_name=u"系统消息"
        verbose_name_plural=u"系统消息"
    def __unicode__(self):
        return self.text
class Address(models.Model):
    xcxUserForeign = models.ForeignKey(XcxUser)
    name=models.CharField(u"姓名",max_length=255)
    detailAddress=models.CharField(u"地址",max_length=255,blank=True)
    contact=models.CharField(u'电话',max_length=255,blank=True)
    province=models.CharField(u'省',max_length=255,blank=True)
    city=models.CharField(u'市',max_length=255,blank=True)
    district=models.CharField(u'区',max_length=255,blank=True)
    countyName=models.CharField(u'国',max_length=255,blank=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name=u"地址信息"
        verbose_name_plural=u"地址信息"





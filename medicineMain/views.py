#coding=utf-8
from django.shortcuts import render

from django.db.models import Q
from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse,HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework import viewsets
from medicine import settings
import serializers
from django.contrib import messages
from django.template.context import RequestContext
from models import *

import json
from django.shortcuts import render_to_response

from django.contrib.auth.decorators import login_required
from rest_framework import  mixins
import hashlib
import os
# Create your views here.
import requests
import hashlib
import os


def getSession():




    return hashlib.sha1(os.urandom(24)).hexdigest()

def getXCXData(appid,secret,js_code):
    r=requests.get('https://api.weixin.qq.com/sns/jscode2session', params={'appid': appid,'secret':secret,'js_code':js_code,'grant_type':'authorization_code'})  # 最基本的GET请求
    data=r.json()
    return data


def wxLogin(request):
    if request.method=='POST':
        code=request.POST.get("code",None)




        if(code):

            data=getXCXData(settings.XCX_ID,settings.XCX_SECRET,code)
            xcxUserRaw=XcxUser.objects.get_or_create(openid=data['openid'])
            xcxUser=xcxUserRaw[0]
            xcxUser.session=data['session_key']
            xcxUser.xcxSession=getSession()
            xcxUser.save()
            List = serializers.UserSerializers(xcxUser, many=False, context={'request': request}).data
            List["is_login"]=xcxUserRaw[1]

            return JsonResponse(List)



        else:
            return HttpResponseBadRequest("错误")


def userInfo(request):
    if request.method == 'POST':
        nickname = request.POST.get("nickname", None)
        gender = request.POST.get("gender", None)
        city = request.POST.get("city", None)
        province = request.POST.get("province", None)
        country = request.POST.get("country", None)
        avatarUrl = request.POST.get("avatarUrl", None)
        session_key = request.POST.get("session_key", None)
        if(session_key):
            xcxUser = get_object_or_404(XcxUser, xcxSession=session_key)
            xcxUser.nickname=nickname
            xcxUser. gender =gender
            xcxUser.city =city
            xcxUser.province =province
            xcxUser.country =country
            xcxUser.avatarUrl = avatarUrl
            xcxUser.save()
            List = serializers.UserSerializers(xcxUser, many=False, context={'request': request}).data

            return JsonResponse(List)
        else:
            return HttpResponseBadRequest(u"参数错误")
    if request.method == 'GET':

        session_key = request.GET.get("session_key", None)
        if(session_key):
            xcxUser = get_object_or_404(XcxUser, xcxSession=session_key)
            List = serializers.UserSerializers(xcxUser, many=False, context={'request': request}).data

            return JsonResponse(List)
        else:
            return HttpResponseBadRequest(u"参数错误")

class CaseHistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get_queryset(self):
        queryset = CaseHistory.objects.all()

        session_key = self.request.query_params.get("session_key")
        if session_key is not None:
            xcxUser=get_object_or_404(XcxUser,xcxSession=session_key)
            queryset = queryset.filter(xcxUserForeign=xcxUser)


        return queryset


    queryset = CaseHistory.objects.all()
    serializer_class = serializers.CaseHistorySerializers

class AddressViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Address.objects.all()

        session_key = self.request.query_params.get("session_key")
        if session_key is not None:
            xcxUser=get_object_or_404(XcxUser,xcxSession=session_key)
            queryset = queryset.filter(xcxUserForeign=xcxUser)


        return queryset


    queryset = Address.objects.all()
    serializer_class = serializers.AddressSerializers



def messages(request):
    messages=Message.objects.all().order_by("-createDateTime")
    list=[]
    for i in messages:
        list.append(i.text)


    return JsonResponse(list,safe=False)
class SymptomViewSet(viewsets.ModelViewSet):
    queryset = Symptom.objects.all()
    serializer_class = serializers.SymptomSerializers

class DisableCSRFCheck(object):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)



def imageUpApi(request):

    if request.method == 'POST':
        outList=[]
        for file in request.FILES.values():
            #file_obj = request.FILES.get('file', None)


            outDict={}


            goodsImage=UserImage.objects.create(image=file)

            outDict['id']=goodsImage.id
            outDict['image']="http://"+request.get_host()+goodsImage.image.url
            outList.append(outDict)



        return JsonResponse(outList,safe=False)
def onLogin(request):
    if request.method =="GET":
        session_key = request.POST.get("session_key", None)
        xcxUser=XcxUser.objects.filter(xcxSession=session_key)
        if(xcxUser.exists()):
            return JsonResponse({"is_login":2})
        else:
            return JsonResponse({"is_login":0})


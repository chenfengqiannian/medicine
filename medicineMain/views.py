#coding=utf-8
from django.core.files import File
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
import random


def getSession():




    return hashlib.sha1(os.urandom(24)).hexdigest()
def getCode(phone):
    code=str(random.randint(1000,9999))
    r = requests.get(' http://qxt.fungo.cn/Recv_center',
                     params={'CpName': "rkdf", 'CpPassword': "rk0902",
                             'DesMobile': phone,"Content":"【短信吧】您的验证码是"+code+".一分钟内有效"})  # 最基本的GET请求

    return code
def getXCXData(appid,secret,js_code):
    r=requests.get('https://api.weixin.qq.com/sns/jscode2session', params={'appid': appid,'secret':secret,'js_code':js_code,'grant_type':'authorization_code'})  # 最基本的GET请求
    data=r.json()
    return data
def getSnsData(appid,secret,code):
    r=requests.get('https://api.weixin.qq.com/sns/oauth2/access_token', params={'appid': appid,'secret':secret,'code':code,'grant_type':'authorization_code'})  # 最基本的GET请求
    data=r.json()
    return data
def getSnsUserData(access_token,openid):
    r=requests.get('https://api.weixin.qq.com/sns/userinfo', params={'access_token': access_token,'openid':openid,'lang':"zh_CN"})  # 最基本的GET请求
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
        queryset = CaseHistory.objects.all().order_by("-modDateTime")

        session_key = self.request.query_params.get("session_key")
        if session_key is not None:
            xcxUser=get_object_or_404(XcxUser,xcxSession=session_key)
            queryset = queryset.filter(xcxUserForeign=xcxUser)


        return queryset


    queryset = CaseHistory.objects.all().order_by("modDateTime")
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
def scrollImage(request):
    messages=ScrollImage.objects.all()
    list=[]
    for i in messages:
        dict={}
        dict["image"]="http://"+request.get_host()+i.image.url
        if(i.imageDetail):
            dict["imageDetail"]="http://"+request.get_host()+i.imageDetail.url
        else:
            dict["imageDetail"] =""
        list.append(dict)


    return JsonResponse(list,safe=False)
def indexImage(request):
    messages=IndexImage.objects.all()
    list=[]
    if(len(messages)>=1):
        list.append("http://"+request.get_host()+messages[0].image.url)
    if (len(messages) >= 2):
        list.append("http://" + request.get_host() + messages[1].image.url)


    return JsonResponse(list,safe=False)
class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = serializers.MessagesSerializers
class SymptomViewSet(viewsets.ModelViewSet):
    queryset = Symptom.objects.all()
    serializer_class = serializers.SymptomSerializers

class DisableCSRFCheck(object):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)



def imageUpApi(request):

    if request.method == 'POST':
        localIds=request.POST.get("localIds",None)
        outList = []
        if(localIds!=None):
            session_key = request.POST.get("session_key")
            a=get_object_or_404(XcxUser,xcxSession=session_key)

            b=requests.get("https://api.weixin.qq.com/cgi-bin/media/get",{"access_token":a.session,"media_id":localIds})
            import os

            # 先定义一个带路径的文件

            filename = localIds+".jpg"
            # 将文件路径分割出来

            file_dir = os.path.join(settings.MEDIA_ROOT,"images",filename)

            # 判断文件路径是否存在，如果不存在，则创建，此处是创建多级目录


                # 然后再判断文件是否存在，如果不存在，则创建
            if not os.path.exists(filename):
                os.system(r'touch %s' % filename)
            with open(filename, 'wb') as fd:
                for chunk in b.iter_content(1024):
                    fd.write(chunk)
            c=File.open(file_dir)
            outDict = {}

            goodsImage = UserImage.objects.create(image=c)

            outDict['id'] = goodsImage.id
            outDict['image'] = "http://" + request.get_host() + goodsImage.image.url
            outList.append(outDict)
        else:






            for file in request.FILES.values():
                #file_obj = request.FILES.get('file', None)


                outDict={}

                file.name=file.field_name



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

def code(request):
    if  request.method =="GET":
        session_key = request.GET.get("session_key", None)
        xcxUser = get_object_or_404(XcxUser, xcxSession=session_key)
        phone = request.GET.get("phone", None)
        if(phone):
            xcxUser.code=getCode(phone)
            xcxUser.save()
            return HttpResponse("ok")

        else:
            return HttpResponseBadRequest("fail")
    if request.method=="POST":
        session_key = request.POST.get("session_key", None)
        xcxUser = get_object_or_404(XcxUser, xcxSession=session_key)
        code = request.POST.get("code", None)
        phone = request.POST.get("phone", None)
        if(code and phone):
            if(code==xcxUser.code):
                xcxUser.phone=phone
                xcxUser.save()
                return HttpResponse(u"成功")
            else:
                return HttpResponseBadRequest(u"验证码错误")
        else:
            return HttpResponseBadRequest(u"参数错误")



import hashlib
from wechat_sdk import WechatBasic
from django.shortcuts import render
from django.http.response import *

from models import *
WEIXIN_TOKEN = 'write-a-value'

WECHAT_TOKEN = 'zqxt'
AppID = ''
AppSecret = ''

# 实例化 WechatBasic
wechat_instance = WechatBasic(
    token=settings.TOKEN,
    appid=settings.SNS_ID,
    appsecret=settings.SNS_SECRET
)

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def wxindex(request):
    if request.method == 'GET':
        # 检验合法性
        # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')

        if not wechat_instance.check_signature(
                signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponseBadRequest('Verify Failed')

        return HttpResponse(
            request.GET.get('echostr', ''), content_type="text/plain")



def index(request):

    indexImage=IndexImage.objects.get(id=2).image.url
    scrollImages=ScrollImage.objects.all()
    scrollImagesList=[]

    code=request.GET.get("code")
    raw=XcxUser.objects.filter(xcxCode=code)
    if(len(raw)>=1):
        xcxSession=raw[0].xcxSession
    else:



        xcxUser = snsuser(code)
        xcxSession=xcxUser.xcxSession












    for i in scrollImages:
        scrollImagesDict = {}
        scrollImagesDict["image"]=i.image.url
        scrollImagesDict["url"]=i.url
        scrollImagesList.append(scrollImagesDict)


    return render(request,"index.html",{"indexImage":indexImage,"imagelist":scrollImagesList,"session_key":xcxSession,"title":u"首页"})


def snsuser(code):
    raw = XcxUser.objects.filter(xcxCode=code)
    if (len(raw) >= 1):
        return raw

    snsdata = getSnsData(settings.SNS_ID, settings.SNS_SECRET, code)


    userdata = getSnsUserData(snsdata["access_token"], snsdata["openid"])
    xcxUserRaw = XcxUser.objects.get_or_create(openid=snsdata['openid'])
    xcxUser = xcxUserRaw[0]
    xcxUser.session = snsdata['access_token']
    xcxUser.xcxSession = getSession()
    xcxUser.nickname = userdata["nickname"].encode("ISO-8859-1")
    xcxUser.gender = userdata["sex"]
    xcxUser.city = userdata["city"].encode("ISO-8859-1")
    xcxUser.province = userdata["province"].encode("ISO-8859-1")
    xcxUser.country = userdata["country"].encode("ISO-8859-1")
    xcxUser.avatarUrl = userdata["headimgurl"]
    xcxUser.save()
    return xcxUser


def addAddress(request):

    return render(request,"addAddress.html")
def bindCellPhone(request):

    return render(request,"bindCellphone.html")

def caseOrder(request):
    session_key = request.GET.get("session_key")
    type=request.GET.get("type")
    xcxUser = get_object_or_404(XcxUser, xcxSession=session_key)
    list=[]
    obj=None;
    if(type=="case"):
        obj=xcxUser.casehistory_set.all()
    if(type=="message"):
        obj=Message.objects.all()
    for i in obj:
        dic={}
        dic["modDateTime"]=i.modDateTime
        if(type=="case"):
            dic["url"]="/caseTest/?id="+str(i.id)
        if (type == "message"):
            dic["url"] = ""
        if (type == "case"):
            dic["text"] =i.physicalCondition
        if (type == "message"):
            dic["text"] = i.text
        list.append(dic)



    if(type=="case"):
        title="历史列表"
    if (type == "message"):
        title = "消息列表"
    return render(request,"caseOrder.html",{"list":list,"title":title})
def caseTest(request):
    if request.method == "GET":
        id=request.GET.get("id",None)
        queryset = Symptom.objects.all()
        list= serializers.SymptomSerializers(queryset,many=True,context={'request': request}).data
        if(id):
            caseHistory=get_object_or_404(CaseHistory,id=id)
            dict = serializers.CaseHistorySerializers(caseHistory, many=False, context={'request': request}).data
            dict["disable"]=True
            for i in list:
                for j in dict["symptom_set"]:
                    if(i["id"]==j["id"]):
                        i["select"]=True


            dict["symptom_set"] = list



            return render(request,"caseTest.html",dict)
        dict={}
        dict["symptom_set"]=list
        dict["disable"] = False
	dict["title"]=u"健康自测"
        return render(request,"caseTest.html",dict)


def myAddress(request):
    session_key = request.GET.get("session_key")
    xcxUser = get_object_or_404(XcxUser, xcxSession=session_key)
    queryset=xcxUser.address_set
    list = serializers.AddressSerializers(queryset, many=True, context={'request': request}).data



    return render(request,"myAddress.html",{"title":u"我的地址","list":list})
def page10070(request):

    code=request.GET.get("code")
    xcxUser=snsuser(code)
    xcxSession=xcxUser.xcxSession
    image=IndexImage.objects.get(id=3)
    avatarUrl=xcxUser.avatarUrl
    nickName=xcxUser.nickname
    return render(request,"page10070.html",{"session_key":xcxSession,"image":image.image.url,"title":u"个人中心","avatarUrl":avatarUrl,"nickName":nickName})
def jssdk(request):
    session_key=request.GET.get("session_key")
    xcxUser = get_object_or_404(XcxUser, xcxSession=session_key)


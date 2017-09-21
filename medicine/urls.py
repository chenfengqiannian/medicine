"""medicine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import settings
from rest_framework import routers
from medicineMain import views

router = routers.DefaultRouter()
router.register(r'casehistory', views.CaseHistoryViewSet)
router.register(r'symptom', views.SymptomViewSet)
router.register(r'address', views.AddressViewSet)
router.register(r'messages', views.MessagesViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
url(r'^messages/', views.messages),
url(r'^scrollimage/', views.scrollImage),
url(r'^indeximage/', views.indexImage),
url(r'^imageupapi/', views.imageUpApi),
    url(r'^wxlogin/', views.wxLogin),
    url(r'^userinfo/', views.userInfo),
url(r'^onlogin/', views.onLogin),
url(r'^code/', views.code),
url(r'^index/', views.index),
url(r'^bindCellPhone/', views.bindCellPhone),
url(r'^caseOrder/', views.caseOrder),
url(r'^caseTest/', views.caseTest),
url(r'^wxindex/', views.wxindex),

url(r'^myAddress/', views.myAddress),
url(r'^page10070/', views.page10070),
url(r'^addAddress/', views.addAddress),


url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT})
]

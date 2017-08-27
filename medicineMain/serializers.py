#coding=utf-8
from django.contrib.auth.models import User, Group
from models import *
from rest_framework import serializers
from django.shortcuts import render_to_response,render,get_object_or_404



class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=XcxUser
        exclude=('passWord','openid',"session")
class SymptomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        exclude = ('CaseHistoryForeign',)

class ImageSerializers(serializers.ModelSerializer):

    class Meta:
        model=UserImage
        exclude = ('caseHistotyForeign',)


class CaseHistorySerializers(serializers.ModelSerializer):
    symptom_set=SymptomSerializers(many=True,read_only=True)
    userimage_set=ImageSerializers(many=True,read_only=True)

    def create(self, validated_data):

        image1=self.initial_data.get("image1",None)
        image2=self.initial_data.get("image2", None)
        symptom=self.initial_data.get("symptom",None)
        session_key = self.initial_data.get("session_key")
        xcxUser = get_object_or_404(XcxUser, xcxSession=session_key)
        caseHistory = CaseHistory.objects.create(xcxUserForeign=xcxUser,**validated_data)
        if(symptom):
            for i in symptom:
                symptomObj=Symptom.objects.get(id=i)
                symptomObj.CaseHistoryForeign.add(caseHistory)
                symptomObj.save()
        if(image1):
            userImage1=UserImage.objects.get(id=image1)
            userImage1.caseHistotyForeign=caseHistory
            userImage1.save()
        if (image2):
            userImage2 = UserImage.objects.get(id=image2)
            userImage2.caseHistotyForeign = caseHistory
            userImage2.save()
        return caseHistory







    class Meta:
        model=CaseHistory
        exclude = ('xcxUserForeign',)
class AddressSerializers(serializers.ModelSerializer):
    def create(self, validated_data):

        session_key=self.initial_data.get("session_key",None)
        xcxUser=get_object_or_404(XcxUser,xcxSession=session_key)


        address = Address.objects.create(xcxUserForeign=xcxUser,**validated_data)
        return address


    class Meta:
        model = Address
        exclude = ('xcxUserForeign',)

class ScrollImageSerializers(serializers.ModelSerializer):

    class Meta:
        model = ScrollImage
        field="__all__"
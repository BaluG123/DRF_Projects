from django.db import models
from django.db.models import fields
from rest_framework import serializers
from . models import Employee

def age_ver(value):
    if value < 18:
        raise serializers.ValidationError("you must be more than 18 to use this application!!")

def name_ver(value):
    if value.lower() == "sunny":
        raise serializers.ValidationError('nikal loude..!')   

def gender_ver(value):
    if len(value) > 6:
        raise serializers.ValidationError('nikal llowde..!')             

class Empserializers(serializers.ModelSerializer):
    name=serializers.CharField(validators=[name_ver])
    age=serializers.IntegerField(validators=[age_ver])
    gender=serializers.CharField(validators=[gender_ver])
    class Meta:
        model=Employee
        fields="__all__"

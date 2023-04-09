from django.db import models
from django.db.models import fields
from rest_framework import serializers
from . models import Employee

def age_ver(value):
    if value < 18 :
        raise serializers.ValidationError('you are not allowed to apply for this job .. under indian constitution rules ')

class Empserializer(serializers.ModelSerializer):
    eage=serializers.IntegerField(validators=[age_ver])
    class Meta:
        model=Employee
        fields="__all__"

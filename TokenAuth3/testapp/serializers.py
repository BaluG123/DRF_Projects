from django.db import models
from rest_framework import serializers
from . models import Employee

def sal_ver(value):
    if value < 1000:
        raise serializers.ValidationError("u are suitable for this job!!")

class Empserializers(serializers.ModelSerializer):
    esal=serializers.IntegerField(validators=[sal_ver])
    class Meta:
        model=Employee
        fields="__all__"
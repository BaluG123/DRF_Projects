from django.db.models import fields
from rest_framework import serializers
from . models import Employee

def age_ver(value):
    if value < 18:
        raise serializers.ValidationError('you must be more than 18 to use this application..!!')

def name_ver(value):
    if value.lower() == "priyanka":
        raise serializers.ValidationError("you cant use this application because developer hate name Priyanka..!")

def addr_ver(value):
    if value.lower() == "bangalore":
        raise serializers.ValidationError("you people are so forweded you guys can't use this application please go away..!")        

class Empserializers(serializers.ModelSerializer):
    eage=serializers.IntegerField(validators=[age_ver])
    eaddr=serializers.CharField(validators=[addr_ver])
    ename=serializers.CharField(validators=[name_ver])
    class Meta:
        model=Employee
        fields="__all__"
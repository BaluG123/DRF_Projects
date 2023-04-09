from django.db.models import fields
from rest_framework import serializers
from . models import Employee

def age_ver(value):
    if value < 18:
        raise serializers.ValidationError("to use this application u must be more than 18..!")

def addr_ver(value):
    if value.lower() == 'bangalore':
        raise serializers.ValidationError("we are not accepting students from this city..!")

class Empserializers(serializers.ModelSerializer):
    eage=serializers.IntegerField(validators=[age_ver])
    eaddr=serializers.CharField(validators=[addr_ver])
    class Meta:
        model=Employee
        fields="__all__"


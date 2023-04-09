from django.db.models import fields
from rest_framework import serializers
from . models import Employee

def age_ver(value):
    if value < 18:
        raise serializers.ValidationError("nikal loude..!")

class Empserializers(serializers.ModelSerializer):
    age=serializers.IntegerField(validators=[age_ver])
    class Meta:
        model=Employee
        fields="__all__"
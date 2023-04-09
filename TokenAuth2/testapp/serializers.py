from django.db import models
from django.db.models import fields
from rest_framework import serializers
from . models import Student

def ver_age(value):
    if value < 18:
        raise serializers.ValidationError('nikal lowde..!')

class Studentserializer(serializers.ModelSerializer):
    age=serializers.IntegerField(validators=[ver_age])
    class Meta:
        model=Student
        fields="__all__"

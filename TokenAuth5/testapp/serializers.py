from django.db import models
from django.db.models import fields
from rest_framework import serializers
from . models import Student

def age_var(value):
    if value < 18:
        raise serializers.ValidationError('you motherfucking bitch..!')

class StudentSerializers(serializers.ModelSerializer):
    age=serializers.IntegerField(validators=[age_var])
    class Meta:
        model=Student
        fields="__all__"
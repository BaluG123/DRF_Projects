from django.db import models
from rest_framework import serializers
from . models import Employee

class Empserializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"
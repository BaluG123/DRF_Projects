from django.db import models
from django.db.models import fields
from rest_framework import serializers
from . models import Employee

class Empserializers(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"
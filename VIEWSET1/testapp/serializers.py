from django.core.exceptions import ValidationError
from django.db import models
from rest_framework import serializers
from testapp.models import Student

def age_ver(value):
    if int(value) < 19 :
        raise ValidationError('please do verify once , you are not allowed to enter this college :) sorry!')


class Studentserilizer(serializers.ModelSerializer):
    age=serializers.CharField(validators=[age_ver])
    class Meta:
        model=Student
        fields="__all__"
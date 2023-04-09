from django.core.exceptions import ValidationError
from django.db import models
from rest_framework import fields, serializers
from . models import Employee

#INBUILT VALIDATION!
    #def age_verification(value):
    #   if value < 18 :
    #       raise serializers.ValidationError('you are not suitable for this job !!') 

class Empserializer(serializers.ModelSerializer):
    #eage=serializers.IntegerField(validators=[age_verification])   
    class Meta:
        model=Employee
        fields="__all__"         
    #FIELD LEVEL VALIDATION..!    
    #def validate_eage(self,value):
    #   if value < 18:
    #       raise serializers.ValidationError('you are too small apply this job..!')

    #OBJECT LEVEL VALIDATION!!
    def validate(value,data):
        age=data.get('eage')
        if age < 18 :
            raise serializers.ValidationError("fuck you bosdik..!")
        return data   

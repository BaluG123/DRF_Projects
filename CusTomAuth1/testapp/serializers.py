from rest_framework import serializers
from . models import Employee

def age_ver(value):
    if value<18:
        raise serializers.ValidationError("to use this application u must be ,ore thyan !8..")

class Empserializers(serializers.ModelSerializer):
    age=serializers.IntegerField(validators=[age_ver])
    class Meta:
        model=Employee
        fields="__all__"
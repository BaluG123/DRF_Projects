from django.shortcuts import render
from rest_framework import serializers
from . models import Employee
from . serializers import Empserializers
from rest_framework.authentication import TokenAuthentication
from . permissions import IswriteOnly,IsReadonly,SuperCheck
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class WriteCheck(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Empserializers
    authentication_classes=[TokenAuthentication]
    permission_classes=[IswriteOnly]

class ReadCheck(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Empserializers
    authentication_classes=[TokenAuthentication] 
    permission_classes=[IsReadonly]  

class SuperCheck(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Empserializers
    authentication_classes=[TokenAuthentication]
    permission_classes=[SuperCheck]     
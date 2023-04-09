from django.shortcuts import render
from . models import Employee
from rest_framework.viewsets import ModelViewSet
from . serializers import Empserializer

# Create your views here.
class testVIEWSET(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Empserializer
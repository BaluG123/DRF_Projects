from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . models import Employee
from . serailizers import Empserializer

# Create your views here.
class Testpostman(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Empserializer
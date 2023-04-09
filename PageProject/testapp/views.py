from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from . models import Employee
from . pagination import Mypagination
from . serializers import Empserializer

# Create your views here.
class Page_View(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=Empserializer
    pagination_class=Mypagination
   


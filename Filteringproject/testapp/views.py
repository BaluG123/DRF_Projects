from re import M
from django.shortcuts import render
from rest_framework import serializers
from . models import Employee
from . serializers import Empserializers
from rest_framework.generics import ListAPIView

# Create your views here.
'''
class FilterView(ListAPIView):
    #queryset=Employee.objects.all()
    serializer_class=Empserializers
    def get_queryset(self):
        qs=Employee.objects.all()
        name=self.request.GET.get('ename')
        if name is not None:
            qs=qs.filter(ename__icontains=name)
        return qs    
'''

class FilterView(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=Empserializers
    search_fields=('^ename',)
    ordering_fields=['ename','eage']
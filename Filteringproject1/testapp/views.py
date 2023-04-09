from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . models import Student
from . serializers import StudentSerializers

# Create your views here.
class searchOrderingfilter(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    search_fields=('^name',)
    ordering_fields=('no',)
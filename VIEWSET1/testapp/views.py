from django.shortcuts import render
from . models import Student
from . serializers import Studentserilizer
from rest_framework.viewsets import ViewSet,ModelViewSet

# Create your views here.
class TestViewset(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Studentserilizer
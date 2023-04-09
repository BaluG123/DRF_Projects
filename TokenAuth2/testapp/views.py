from django.shortcuts import render
from . models import Student
from . serializers import Studentserializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ApiView(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Studentserializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
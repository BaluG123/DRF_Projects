from django.shortcuts import render
from rest_framework import permissions
from . serializers import Empserializers
from . models import Employee
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class TestTokenAuth(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Empserializers
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
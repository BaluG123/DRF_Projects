from django.shortcuts import render
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from . models import Employee
from . serializers import Empserializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TokenView(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Empserializers
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
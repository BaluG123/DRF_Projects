from django.shortcuts import render
from rest_framework import serializers
from . models import Employee
from . serializers import Empserializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from . permissions import IsWrite 


# Create your views here.
class ApiCheck(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Empserializers
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsWrite]
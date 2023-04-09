from django.shortcuts import render
from rest_framework import authentication
from . models import Student
from . serializers import StudentSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,IsAdminUser,IsAuthenticated,AllowAny


# Create your views here.
class Checkauth(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    #permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    #permission_classes=[IsAdminUser]
    #permission_classes=[IsAuthenticated]
    permission_classes=[AllowAny]
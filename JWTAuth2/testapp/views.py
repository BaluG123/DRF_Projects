from django.shortcuts import render
from rest_framework import authentication
from . models import Employee
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,IsAuthenticatedOrReadOnly
from . serializers import Empserializers
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ApiCheck(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Empserializers
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]

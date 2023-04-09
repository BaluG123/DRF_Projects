from django.shortcuts import render
from . models import Employee
from . serializers import Empserializers
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class Empcrudcbv(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Empserializers
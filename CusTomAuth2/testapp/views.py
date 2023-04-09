from django.shortcuts import render
from . models import Employee
from . serializers import Empserializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions,IsAdminUser,IsAuthenticated,DjangoModelPermissionsOrAnonReadOnly,AllowAny
from rest_framework.viewsets import ModelViewSet
from . permissions import IsreadOnly,IsSuper

# Create your views here.
class CheckApi(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Empserializers
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]

class ReadCheck(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Empserializers
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsreadOnly] 

class SuperCheck(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Empserializers
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsSuper]       
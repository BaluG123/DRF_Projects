from django.shortcuts import render
from . models import Employee
from . serializers import Empserializers
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from . permissions import IsWriteOnly
from . authentications import CustomAuth

# Create your views here.
class ApiCheck(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Empserializers
    #authentication_classes=[JSONWebTokenAuthentication]
    #authentication_classes=[TokenAuthentication]
    #permission_classes=[IsAuthenticated]
    authentication_classes=[CustomAuth]
    permission_classes=[IsWriteOnly]
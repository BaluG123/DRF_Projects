from django.shortcuts import render
from . models import Employee
from . serializers import Empserializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ViewSet,ModelViewSet
from . permissions import CheckRead,CheckWrite

# Create your views here.
class TestToken(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Empserializers
    authentication_classes=[TokenAuthentication]
    #permission_classes=[AllowAny] ---> anyone can access our endpoints , without authentication and autherization
    #permission_classes=[IsAuthenticated]---> only authenticated persons can abe to access end points
    #permission_classes=[IsAuthenticatedOrReadOnly]--->for read operations(GET,READ,OPTION) no need authentication and autheraization, for write operations u must authenticate!!
    #permission_classes=[IsAdminUser]--> only admin can access [normal user->staff-status(ON)==ADMIN],ADMIN CANT EDIT IN ADMIN INTERFACE..
    #permission_classes=[DjangoModelPermissions]--> TO ACCES END POINT AUTHENTICATION MUST BE REQUIRED..!!
    #                                           --> TO ACCESSS GET RESPONSE AUTHENTICATION REQUIRED BUT NOT MODEL ERMISSION
    #                                           --> TO ACCESS POST,PUT,PATCH,DELETE (BOTH AUTHENTICATION AND PERMISIIONS REQUIRED!)
    #                                           --> POST (add permission) , PUT PATCH(change permission), DELETE(delete permission)
    #                                           --> go to admin interface (after clicking user) below .. permisiions testapp|employee|can (add,change,delete) employee
    #permission_classes=[DjangoModelPermissionsOrAnonReadOnly] #--> it same as the djangomodelpermisiiions except 
    # anyone can access read operations(GET[no authentication is required!],HEAD,OPTION), to perform write operations authentication is must
    #for superuser no need any permisiions...
    permission_classes=[CheckWrite]

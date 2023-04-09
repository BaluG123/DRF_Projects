from django.shortcuts import render
from . models import Employee
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from . serializers import Empserializers
from rest_framework .viewsets import ModelViewSet

# Create your views here.
class Emp_view(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Empserializers
    #authentication_classes=[BasicAuthentication]
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]

def logout_view(request):
    return render(request,'testapp/logout.html')    
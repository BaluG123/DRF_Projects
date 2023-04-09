from django.shortcuts import render
from . models import Book,Author
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from . serializers import Authorserializers,Bookserializers

# Create your views here.
class AuthorlistCreateview(ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=Authorserializers

class AuthorView(RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=Authorserializers
    lookup_field="id"

class Booklistcreateview(ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=Bookserializers

class Bookview(RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=Bookserializers  
    lookup_field="id"          
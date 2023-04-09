from django.shortcuts import render
from . models import Author,Book
from . serializers import Authserailizers,BookSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.
class AuthorList_View(ListAPIView):
    queryset=Author.objects.all()
    serializer_class=Authserailizers

class Author_view(RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=Authserailizers
    lookup_field="id"   

class BookList_View(ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializers

class Book_view(RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializers 
    lookup_field="id"      
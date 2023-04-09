from django.db import models
from django.db.models import fields
from rest_framework import serializers
from . models import Author,Book

class Bookserializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"  

class Authorserializers(serializers.ModelSerializer):
    books_by_author=Bookserializers(read_only=True,many=True)
    class Meta:
        model=Author
        fields="__all__"
      
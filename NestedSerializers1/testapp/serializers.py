from django.db import models
from django.db.models import fields
from rest_framework import serializers
from . models import Book,Author

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"

class Authserailizers(serializers.ModelSerializer):
    books_by_author=BookSerializers(read_only=True,many=True)
    class Meta:
        model=Author
        fields="__all__"        
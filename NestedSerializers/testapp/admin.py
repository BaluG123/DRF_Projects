from django.contrib import admin
from . models import Author,Book

class AuthorAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','subject']

class Bookadmin(admin.ModelAdmin):
    list_display=['id','author','release_date','rating']

# Register your models here.
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,Bookadmin)
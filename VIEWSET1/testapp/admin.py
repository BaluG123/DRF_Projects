from django.contrib import admin
from . models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','no','name','age','gender','gmail']
    search_fields=('name','gender')
    list_filter=('age','name')


# Register your models here.
admin.site.register(Student,StudentAdmin)
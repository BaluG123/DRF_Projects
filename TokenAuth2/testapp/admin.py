from django.contrib import admin
from . models import Student

class studentAdmin(admin.ModelAdmin):
    list_display=['id','no','name','age','gender']
    list_filter=('name','age')
    search_fields=('name',)

# Register your models here.
admin.site.register(Student,studentAdmin)
from django.contrib import admin
from . models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['no','name','age','addr']
    list_filter=('name','addr')

# Register your models here.
admin.site.register(Employee,EmployeeAdmin)
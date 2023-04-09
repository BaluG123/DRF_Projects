from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from . models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','eage','esal','eaddr']

# Register your models here.
admin.site.register(Employee,EmployeeAdmin)
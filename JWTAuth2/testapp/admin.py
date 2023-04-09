from django.contrib import admin
from . models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','eage','eaddr']
    list_filter=('ename','eaddr')

# Register your models here.
admin.site.register(Employee,EmployeeAdmin)
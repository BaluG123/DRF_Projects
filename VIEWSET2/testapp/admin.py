from django.contrib import admin
from . models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','eage','egender']
    list_filter=('eno','ename','eage','egender')
    search_fields=('ename',)

# Register your models here.

admin.site.register(Employee,EmployeeAdmin)
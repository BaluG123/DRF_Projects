from django.contrib import admin
from  . models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','eage','eaddr']
    list_filter=('ename','eage','eaddr')
    search_fields=('ename','eaddr')

# Register your models here.
admin.site.register(Employee,EmployeeAdmin)
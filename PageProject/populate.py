import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','PageProject.settings')
import django
django.setup()

from testapp.models import *
from random import *
from faker import Faker
fake=Faker()
def populate(n):
    for i in range(n):
        fno=randint(1,1000)
        fname=fake.name()
        fage=randint(20,40)
        faddr=fake.city()
        emp_list=Employee.objects.get_or_create(eno=fno,ename=fname,eage=fage,eaddr=faddr)
populate(1000)        



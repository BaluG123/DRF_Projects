import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Filteringproject.settings')

import django
django.setup()
from random import *
from testapp.models import *
from faker import Faker
fake=Faker()

def populate(n):
    for i in range(n):
        fno=randint(1,200)
        fname=fake.name()
        fage=randint(20,35)
        faddr=fake.city()
        emp_list=Employee.objects.get_or_create(eno=fno,ename=fname,eage=fage,eaddr=faddr)
populate(200)        



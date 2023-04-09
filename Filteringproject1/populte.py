import os
from re import S

from django.core.exceptions import ImproperlyConfigured
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Filteringproject1.settings')
import django
django.setup()
from random import *
from testapp.models import *
from faker import Faker
fake=Faker()

def populate(n):
    for i in range(n):
        fno=randint(1,100)
        fname=fake.name()
        fage=randint(20,35)
        fgender=fake.random_element(elements=('male','female'))
        student_list=Student.objects.get_or_create(no=fno,name=fname,age=fage,gender=fgender)
populate(200)        

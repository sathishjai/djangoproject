import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cruddemo.settings')

import django
django.setup()

from crudapp.models import *
from faker import Faker
from random import *
faker=Faker()

def generate(n):
    for i in range(n):
        fsno=randint(1,1000)
        fsname=faker.name()
        fsclass=randint(1,30)  
        fsaddress=faker.city()
        stu_record=student.objects.get_or_create(sno=fsno,sname=fsname,saddress=fsaddress)

generate(20)


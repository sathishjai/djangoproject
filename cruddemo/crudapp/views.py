from django.shortcuts import render
from crudapp.models import student
# Create your views here.

def retrieve_view(request):
#    student=
    return render(request,'crudapp/index.html',{'student':student.objects.all()})

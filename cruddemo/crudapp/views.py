from django.shortcuts import render
from crudapp.models import student
from crudapp.forms import studentform
# Create your views here.

def retrieve_view(request):
#    student=
    return render(request,'crudapp/index.html',{'student':student.objects.all()})

def create_view(request):
    form=studentform()
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'crudapp/create.html',{'form':form})


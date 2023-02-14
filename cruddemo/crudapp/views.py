from django.shortcuts import render,redirect
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
            return redirect('/check')
    return render(request,'crudapp/create.html',{'form':form})

def delete_view(request,id):
    student.objects.get(id=id).delete()
    return redirect('/check')

#delete--->id
#update--->id

def update_view(request,id):
    student=student.object.get(id=id)
    if request.method == 'POST':
        form=studentform(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request,'crudapp/update.html',{'student':student})

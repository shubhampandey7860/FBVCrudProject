from django.shortcuts import render
from app.forms import *
from django.http import HttpResponseRedirect
from app.models import *
# Create your views here.
def add_show(request):
    if request.method=='POST':
        form = StudentForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password=form.cleaned_data['password']
            reg = User(name=name,password=password,email=email)
            reg.save()
    else:
        form = StudentForm() 
    stu = User.objects.all()   
    return render(request,'app/app_and_show.html',{'form':form,'stu':stu})



def Update_data(request,id):
    if request.method=='POST':
         pi = User.objects.get(pk=id)
         fm = StudentForm(request.POST,instance=pi)
         if fm.is_valid():
             fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentForm(instance=pi)
                 
        
    return render(request,'app/updatestudent.html',{'form':fm})


def delete_data(request,id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
        

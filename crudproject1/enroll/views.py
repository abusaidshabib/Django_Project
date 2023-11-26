from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_show(request):
    student = User.objects.all()
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # short and easy way
            # fm.save()
            
            # check every field helps to add specific fields
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg = User(name=name, email=email,password=password)
            reg.save()
            # this will send a blank form to template after submitting the form this will clean the form
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':student})

# this function wil update/edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':fm})


# This function will delete data
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        print(pi)
        pi.delete()
        return HttpResponseRedirect('/')

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from mysite.models import Designation


def index(request):
    return render(request,'mysite/index.html')

def addDepartment(request):
    return render(request,'mysite/departments/adddept.html')
def ViewDepartment(request):
    return render(request,'mysite/departments/viewdept.html')
def DeleteDepartment(request):
    return render(request,'mysite/departments/deldept.html')


def addDesignation(request):
    if request=='POST':
        print(request.POST.get("Desname"))
        Desname=request.POST.get("Desname")
        select=request.POST.get("select")
        c=Designation(DesignationName=Desname,Status=select)
        c.save()
        return render(request,'mysite/designations/add.html')

    else:
        return render(request, 'mysite/designations/add.html')

def ViewDesignation(request):
    return render(request,'mysite/designations/view.html')
def RemoveDesignation(request):
    return render(request,'mysite/designations/delete.html')



def addOffice(request):
    return render(request,'mysite/offices/addoffice.html')
def viewOffice(request):
    return render(request,'mysite/offices/viewoffices.html')
def RemoveOffice(request):
    return render(request,'mysite/offices/deleteoffice.html')



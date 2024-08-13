from django.shortcuts import render,HttpResponse
from .models import Product,StudentRegisteration
from .forms import StudentForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def index(requext):
    return render(requext,'index.html')

def product(request):
    product_data = Product.objects.all() # this is a qurey of orm
    context = {
        'product':product_data
    }
    return render(request,'Products.html',context)

def signuphandle(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password1']
        user = User(username=username,email=email)
        user.set_password(password)
        user.save()
        return HttpResponse('User Account Successfully created !!')
    return render(request,'signup.html')

def loginhandle(request):
    return render(request,'login.html')


def Student(request):
    if request.method == "POST":
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            fullname = request.POST['FullName']
            email = request.POST['Email']
            roll_no = request.POST['Roll_no']
            mobile_no = request.POST['Mobile_No']
            address = request.POST['Address']
            pin_code = request.POST['Pin_code']
            image = request.FILES['Image']
            StudentRegisteration(FullName = fullname , Email = email , Roll_no = roll_no , Mobile_No = mobile_no , Address = address , Pin_code = pin_code , Image = image).save()
            messages.success(request,'Your Form Successfull Submited !!')
    form = StudentForm()
    context = {
        'form':form
    }
    return render(request,'Student.html',context)

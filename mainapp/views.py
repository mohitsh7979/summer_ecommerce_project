from django.shortcuts import render,HttpResponse
from .models import Product
from django.contrib.auth.models import User

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

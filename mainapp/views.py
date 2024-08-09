from django.shortcuts import render
from .models import Product

# Create your views here.


def index(requext):
    return render(requext,'index.html')

def product(request):
    product_data = Product.objects.all()
    print(product_data,"product data")
    context = {
        'product':product_data
    }
    return render(request,'Products.html',context)

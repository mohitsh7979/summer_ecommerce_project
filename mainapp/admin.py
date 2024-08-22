from django.contrib import admin
from .models import Product,StudentRegisteration,Cart

# Register your models here.

# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','description','image','size','category','is_avaliable']


@admin.register(StudentRegisteration)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','FullName','Email','Roll_no','Mobile_No','Address','Pin_code','Image']
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']
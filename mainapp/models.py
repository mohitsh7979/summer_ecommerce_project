from django.db import models

# Create your models here.

CATEGORY_CHOICE = [
    
    ("mens","mens"),
    ("womens","womens"),
    ("kids","kids"),
    ("electronic","electronic"),
    ("special_product","special_product")
]

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    size = models.CharField(max_length=10)
    category = models.CharField(choices=CATEGORY_CHOICE,max_length=50)
    is_avaliable = models.BooleanField()
    
    def __str__(self):
        return self.title
    
    
class StudentRegisteration(models.Model):
    FullName = models.CharField(max_length=50)
    Email = models.EmailField()
    Roll_no = models.IntegerField()
    Mobile_No = models.IntegerField()
    Address = models.TextField()
    Pin_code = models.IntegerField()
    Image = models.ImageField(upload_to='media')
    

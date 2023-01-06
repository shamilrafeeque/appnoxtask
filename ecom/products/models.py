from django.db import models

# Create your models here.
class Products(models.Model):
    product_name =models.CharField(max_length=200,unique=True)
    description  =models.CharField(max_length=200,unique=True)
    price        =models.IntegerField()
    images       =models.ImageField(upload_to='photos/products')
    stock        =models.IntegerField()
    is_available =models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.product_name

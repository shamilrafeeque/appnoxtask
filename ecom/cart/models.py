from django.db import models
from products.models import Products
from accounts.models import Account
# Create your models here.
class cart(models.Model):
    item=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    is_active=models.BooleanField(default=True)
    
    
    def __str__(self):
        return  str(self.item)
    
    
    
     
    
    
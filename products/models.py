from django.db import models
import datetime 
# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length= 100)
    description = models.TextField(max_length= 2000, null= True, blank= True)
    price = models.PositiveIntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/', null=True)
    def __str__(self):
        return self.title
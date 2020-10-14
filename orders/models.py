from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()
# Create your models here.
class Order(models.Model):
    address = models.CharField(max_length=150, help_text='Enter Your Address')
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)

    def __str__(self):
        return str(self.user)
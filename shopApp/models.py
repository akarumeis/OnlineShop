from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products', kwargs={'product_pk':self.pk})
    
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="image/%Y/%m/%d")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


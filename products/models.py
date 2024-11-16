from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
import os
from datetime import datetime

User = settings.AUTH_USER_MODEL
    
def image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')  # Format: YYYYMMDD_HHMMSS
    filename = f'{timestamp}.{ext}'

    return os.path.join('images', filename)

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to=image_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    CATEGORY_CHOICE = (
        ('shirt','shirt'),
        ('t-shirt','t-shirt'),
        ('trousers','trousers'),
        ('jacket','jacket'),
        ('shorts','shorts'),
        ('dress','dress'),
        ('jeans','jeans'),
        ('others','others')
    ) 
    category = models.CharField(choices=CATEGORY_CHOICE,max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    class Meta:
        ordering = ['category','price']

    def __str__(self):
        return self.name
    

class Stock(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    small = models.IntegerField(validators=[MinValueValidator(0)])
    medium = models.IntegerField(validators=[MinValueValidator(0)])
    large = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return str(self.product) + "_stock"
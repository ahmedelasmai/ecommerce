from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/static/products/images/products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        ordering = ['category','price']

    def __str__(self):
        return self.name

class Stock(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    small = models.IntegerField()
    medium = models.IntegerField()
    large = models.IntegerField()

    def __str__(self):
        return str(self.product) + "_stock"
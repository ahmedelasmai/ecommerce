from django.shortcuts import render
from django.views.generic import ListView

from products.models import Products, Categories

def index(request):
    return render(request,'products/index.html')

class products(ListView):
    paginate_by = 20
    model = Products
    template_name = 'products/products.html'

def product(request):
    return render(request, 'products/product.html')






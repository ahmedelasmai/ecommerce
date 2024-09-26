from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView

from products.models import Products

class products(ListView):
    paginate_by = 20
    model = Products
    template_name = 'products/products.html'

class product(DetailView):
    model = Products
    template_name = 'products/product.html'
    context_object_name = 'product'



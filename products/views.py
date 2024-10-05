from django.db import transaction
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from django.views.generic import ListView,CreateView
from django.contrib import messages 
from .models import Products,Stock
from .forms import ProductForm,ProductModelForm,StockModelForm
from django.contrib.auth.decorators import login_required

class products(ListView):
    paginate_by = 20
    model = Products
    template_name = 'products/products.html'

@login_required
def upload(request): 
    if request.method == 'POST':
        product_form = ProductModelForm(request.FILES)
        stock_form = StockModelForm()
        
        if product_form.is_valid() and stock_form.is_valid():
            product = product_form.save(commit=False)
            product.user = request.user
            product.save()
            stock = stock_form.save(commit=False)
            stock.product = product
            stock.save()
            return redirect('products')
    else:
        product_form = ProductModelForm()
        stock_form = StockModelForm()

    context = {
        'product_form': product_form,  
        'stock_form': stock_form,
    }
    return render(request,'products/upload.html',context=context)


def product(request,pk):
    product = get_object_or_404(Products,pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            size = form.cleaned_data['size']
            quantity = form.cleaned_data['quantity']
            with transaction.atomic():
                #select_for_update Locks the stock row for this size to avoid race conditions
                stock_object = Stock.objects.select_for_update().get(product=pk)
                stock = getattr(stock_object,size)

                if quantity > stock:
                    form.add_error(None, f"Not enough in stock. There is only {stock} in stock")
                else:
                    new_value = stock - quantity                                            #data type error ?
                    setattr(stock_object,size,new_value)
                    stock_object.save()

                    cart = request.session.get('cart', {})

                    if str(product.id) in cart:
                        cart[str(product.id)]['quantity'] += int(quantity)
                        cart[str(product.id)]['price'] = str(format(product.price * cart[str(product.id)]['quantity'],'.2f'))
                    else:
                        product.price = float(product.price) * quantity
                        cart[str(product.id)] = {
                            'name': product.name,
                            'price': str(format(product.price,'.2f')),
                            'quantity': quantity,
                            'size': size,
                            'image_location': str(product.image.url)
                        }   
                    request.session['cart'] = cart
                    request.session.modified = True
                    messages.success(request,f'{product.name} added to cart')
                    return redirect('product',pk=pk)
                    
    else:
        form = ProductForm()
    return render(request,'products/product.html',{'product':product,'form':form})

    



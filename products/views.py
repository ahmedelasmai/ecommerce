from django.db import transaction
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView
from django.contrib import messages 
from .models import Products,Stock
from .forms import ProductForm

class products(ListView):
    paginate_by = 20
    model = Products
    template_name = 'products/products.html'

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
                    new_value = stock - int(quantity)                                               #data type error ?
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

    



from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .models import Products, Stock
from .forms import ProductForm, ProductModelForm, StockModelForm

#lists products (multiple) 
class products(ListView):
    paginate_by = 20
    model = Products
    template_name = 'products/products.html'

@login_required
def upload(request): 
    if request.method == 'POST':
        product_form = ProductModelForm(request.POST,request.FILES)
        stock_form = StockModelForm(request.POST)
        
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

#single product 
def product(request,pk):
    product = get_object_or_404(Products, pk=pk)
    #adding product to cart
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            size = form.cleaned_data['size']
            quantity = form.cleaned_data['quantity']
            with transaction.atomic():
                stock_object = Stock.objects.select_for_update().get(product=pk)
                stock = getattr(stock_object, size)
                #update amount in stock when product added to cart
                if quantity >= stock:
                    form.add_error(None, f"Not enough in stock. There is only {stock} in stock")
                else:
                    new_value = stock - quantity
                    setattr(stock_object, size, new_value)
                    stock_object.save()
                    
                    #create/add to cart (session)
                    cart = request.session.get('cart', {})
                    product_id = str(product.id)

                    if product_id in cart:
                        cart[product_id]['quantity'] += quantity
                        cart[product_id]['price'] = f"{product.price * cart[product_id]['quantity']:.2f}"
                    else:
                        cart[product_id] = {
                            'name': product.name,
                            'price': f"{product.price * quantity:.2f}",
                            'quantity': quantity,
                            'size': size,
                            'image_location': str(product.image.url)
                        }   
                    request.session['cart'] = cart
                    request.session.modified = True
                    messages.success(request, f'{product.name} added to cart')
                    return redirect('product', pk=pk)
                    
    else:
        form = ProductForm()
    return render(request,'products/product.html',{'product':product,'form':form})

    



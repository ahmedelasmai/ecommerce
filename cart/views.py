from django.shortcuts import render,redirect
from django.db import transaction
from products.models import Stock

def index(request):
    cart = request.session.get('cart', {})
    overall_price = 0.00
    for product in cart.values():
        overall_price += float(product['price'])
    return render(request, 'cart/index.html',{'cart': cart, 'overall_price': format(overall_price,'.2f')}) 

def remove_cart_item(request,id=id):
    cart = request.session.get('cart', {})
    
    if id in cart:
        with transaction.atomic():
            stock = Stock.objects.select_for_update().get(product=int(id))
            current_quantity = getattr(stock, cart[id]['size'], 0)
            updated_quantity = current_quantity + cart[id]['quantity']
            setattr(stock,cart[id]['size'],updated_quantity)
            stock.save()

            del cart[id]
            request.session['cart'] = cart
            request.session.modified = True
            

    
    return redirect('index')
    
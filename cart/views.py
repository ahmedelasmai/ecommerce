from django.shortcuts import render, redirect
from django.db import transaction
from django.conf import settings
from django.contrib.auth.decorators import login_required

from products.models import Stock

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def stripe_checkout(request):
    line_items = []
    cart = request.session.get("cart", {})
    for product_id, product in cart.items():
        price = float(
            product["price"]
        )  # stripe uses integer for price. (product.price) is a string with decimal
        price = int(price * 100)
        line_items.append(
            {
                "price_data": {
                    "currency": "gbp",
                    "product_data": {
                        "name": product["name"],
                    },
                    "unit_amount": price,
                },
                "quantity": product["quantity"],
            }
        )
    try:
        # Create a Stripe Checkout Session with multiple line items
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url="http://127.0.0.1:8000/cart/success/",
            cancel_url="http://127.0.0.1:8000/cart/cancel/",
        )
        return redirect(session.url)

    except Exception as e:
        print(f"Error: {str(e)}")


@login_required
def success(request):
    return render(request, "cart/success.html")


@login_required
def cancel(request):
    return render(request, "cart/cancel.html")


@login_required
def index(request):
    cart = request.session.get("cart", {})
    overall_price = 0.00
    for product in cart.values():
        product_price = float(product["price"]) * product["quantity"]
        overall_price += product_price
    overall_price = format(overall_price, ".2f")
    return render(
        request,
        "cart/index.html",
        {"cart": cart, "overall_price": overall_price},
    )


@login_required
def remove_cart_item(request, id=id):
    cart = request.session.get("cart", {})

    if id in cart:
        with transaction.atomic():
            stock = Stock.objects.select_for_update().get(product=int(id))

            current_quantity = getattr(stock, cart[id]["size"], 0)
            updated_quantity = current_quantity + cart[id]["quantity"]

            setattr(stock, cart[id]["size"], updated_quantity)
            stock.save()

            del cart[id]
            request.session["cart"] = cart
            request.session.modified = True

    return redirect("index")

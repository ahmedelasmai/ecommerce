from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("remove_cart_item/<str:id>/", views.remove_cart_item, name="remove_cart_item"),
    path("stripe_checkout/", views.stripe_checkout, name="stripe_checkout"),
    path("success/", views.success, name="success"),
    path("cancel/", views.cancel, name="cancel"),
]

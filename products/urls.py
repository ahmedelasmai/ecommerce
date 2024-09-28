from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products.as_view(), name='products'),
    path('product/<int:pk>/',views.product, name='product')
]
    

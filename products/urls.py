from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('products/', views.products.as_view(), name='products'),
    path('product/', views.product, name='product'),
]
    

from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path("products/", views.products.as_view(), name="products"),
    path("product/<int:pk>/", views.product, name="product"),
    path("upload/", views.upload, name="upload"),
    path("", RedirectView.as_view(url="products/", permanent=True)),
]

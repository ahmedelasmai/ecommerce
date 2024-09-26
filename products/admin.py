from django.contrib import admin

from .models import Products, Categories, Stock

admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Stock)
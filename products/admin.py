from django.contrib import admin

from .models import Products,Stock

admin.site.register(Products)
admin.site.register(Stock)
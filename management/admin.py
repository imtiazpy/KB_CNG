from django.contrib import admin
from .models import Product, Stock, Sale, Unit


admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Sale)
admin.site.register(Unit)
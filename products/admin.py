from django.contrib import admin
from .models import Product, Category, Supplier

admin.site.register(Category)
admin.site.register(Supplier)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock_level']

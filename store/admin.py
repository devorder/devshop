from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'price', 'stock', 'is_available', 'category', 'updated_at')

# Register your models here.
admin.site.register(Product, ProductAdmin)

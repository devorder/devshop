from unicodedata import category
from django.shortcuts import get_object_or_404, render

from category.models import Category
from .models import Product

# Create your views here.
def store(request, category=None):
    categories = None
    products = None
    if category != None:
        category = get_object_or_404(Category, slug=category)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        products = Product.objects.filter(is_available=True)    
    print(categories)
    ctx = {
        'products': products,
        'product_count': products.count()
    }
    return render(request, 'store/store.html', context=ctx)

def product_detail(request, category_slug, product_slug):
    product = None
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    
    ctx = {
        'product':product
    }
    return render(request, 'store/product_detail.html', context=ctx)
from django.shortcuts import render
from .models import Product

def product_list(request, tenant_id):
    products = Product.objects.filter(tenant_id=tenant_id)
    return render(request, 'product_list.html', {'products': products})

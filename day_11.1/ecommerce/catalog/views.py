from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Product


def product_list(request):
    ob_products = Product.objects.all()
    return render(request, 'product_list.html', {'products': ob_products})

def product_detail(request, pk):
    ob_product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': ob_product})

from django.shortcuts import render
from .models import *

# Create your views here.

def show_product(request, product_pk):
    product = Product.objects.filter(category_id = product_pk)
    return render(request, 'product.html', context = {'products': product})

    


def show_shop(request):
    categorys = Category.objects.all()
    return render(request, 'shop.html', context = {'categorys': categorys})
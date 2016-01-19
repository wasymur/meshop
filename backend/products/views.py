from django.shortcuts import render
from django.http import Http404
from models import Product, Category

from django.http import HttpResponse



def product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except:
        raise Http404("Question does not exist")
    context = {'product': product}
    return render(request, 'products/product.html', context)




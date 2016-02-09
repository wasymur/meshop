from django.shortcuts import render_to_response
from django.http import Http404
from models import Product
from django.template import RequestContext
from django.conf import settings


def product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except:
        raise Http404("Product does not exist")
    context = {
        'product': product,
        'MEDIA_URL': settings.MEDIA_URL,
        'user': request.user
    }
    return render_to_response('products/product.html', context, context_instance=RequestContext(request))


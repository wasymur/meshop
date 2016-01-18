from django.shortcuts import render

from django.http import HttpResponse


def product(request, product_id):
    return HttpResponse("lets get you product %s." % product_id)

__author__ = 'wasy'

from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [

    #url(r'^', views.products),

    #url(r'^(?P<category_id>\d*)/$', views.products),

    url(r'^(?P<product_id>\d*)/$', views.product),
]

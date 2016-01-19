__author__ = 'wasy'

from django.conf.urls import url
from django.conf import settings
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

urlpatterns = [

    #url(r'^', views.products),

    #url(r'^(?P<category_id>\d*)/$', views.products),

    url(r'^(?P<product_id>\d*)/$', views.product),
]

# static files:
urlpatterns += staticfiles_urlpatterns() #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
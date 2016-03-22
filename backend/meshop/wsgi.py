"""
WSGI config for meshop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

#import os

#from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meshop.settings")

#application = get_wsgi_application()


import os
import sys
import site
import socket

from django.core.wsgi import get_wsgi_application

# Add the site-packages of the chosen virtualenv to work with
if socket.gethostname() != 'wasy-lap':
    site.addsitedir('/var/www/.virtualenvs/meshopvenv/local/lib/python2.7/site-packages')
    sys.path.append('/var/www/')
    sys.path.append('/var/www/meshop/backend/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'meshop.settings'
# Activate your virtual env
if socket.gethostname() != 'wasy-lap':
    activate_env = os.path.expanduser("/var/www/.virtualenvs/meshopvenv/bin/activate_this.py")
    execfile(activate_env, dict(__file__=activate_env))

application = get_wsgi_application()

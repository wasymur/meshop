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
# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/var/www/.virtualenvs/meshopvenv/local/lib/python2.7/site-packages')
# Add the app's directory to the PYTHONPATH
sys.path.append('/var/www/meshop')
sys.path.append('/var/www/meshop/meshop')
os.environ['DJANGO_SETTINGS_MODULE'] = 'meshop.meshop.settings'
# Activate your virtual env
activate_env=os.path.expanduser("/var/www/.virtualenvs/meshopvenv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

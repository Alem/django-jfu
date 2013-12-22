"""
WSGI config for demo project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys
import site

os.environ['DJANGO_SETTINGS_MODULE'] = 'demo.settings'

SITE_ROOT = os.path.dirname(os.path.dirname( __file__ ))

site.addsitedir( SITE_ROOT + '/venv/local/lib/python2.7/site-packages' )

sys.path.append( SITE_ROOT )

exc_dir = 'scripts' if os.name == 'nt' else 'bin'
venv = '%s/venv/%s/activate_this.py' % (SITE_ROOT, exc_dir )

activate_env = os.path.expanduser( venv )
execfile( activate_env, dict(__file__ = activate_env ))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

from setuptools import setup, find_packages
from os.path import dirname
import jfu

setup(
    name    = 'django-%s' % jfu.__prog__,
    version = jfu.__version__,
    author  = jfu.__author__,
    author_email = "alem@cidola.com",
    description  = jfu.__desc__,
    license      = jfu.__licence__,
    keywords     = "django, jquery file upload, multi-upload",
    url          = "http://packages.python.org/jfu",
    packages     = find_packages(),
    include_package_data = True,
    long_description = open('README.rst').read(),
    classifiers  = [
         'Environment :: Web Environment',
         'Framework :: Django',
         'Intended Audience :: Developers',
         "License :: OSI Approved :: %s" % jfu.__licence__,
         'Operating System :: OS Independent',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2.7',
         'Topic :: Internet :: WWW/HTTP',
         'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

# Django settings for tracker project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ( 
    # ('Your Name', 'your_email@domain.com'),
 )

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'trackme-dev',
        'USER': 'trackme',
        'PASSWORD': 'trackme',
        'HOST': '10.11.208.35',
        'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = None
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = ''

import os
STATIC_DOC_ROOT = os.path.join( os.path.dirname( __file__ ), 'static' )
MEDIA_ROOT = os.path.join( os.path.dirname( __file__ ), 'media' )


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'k_zc^@8l000s#5ni%@4_7w(q+=-x60)br1*^$r+&8y5%1g0l4v'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = ( 
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
 )

MIDDLEWARE_CLASSES = ( 
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
 )

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = ( 
    os.path.join( os.path.dirname( __file__ ), 'templates' )
 )

INSTALLED_APPS = ( 
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'datastore',
    'collector',
    'kml',
    'mapper',
    'shell_plus',
    'world'
 )

SERIALIZATION_MODULES = {
    'json': 'wadofstuff.django.serializers.json'
}


GEOS_LIBRARY_PATH = '/usr/lib/libgeos_c.so'

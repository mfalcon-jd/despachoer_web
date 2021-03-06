# -*- coding: utf-8 -*-
"""
Django settings for despachoer project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+ndy!@a7=5dg2a)9kk^l3ve$wxgm4lb4$oi5rsuu$mhazd29uu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # 'material',
    # 'material.admin',
    #'django_admin_bootstrapped',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'xadmin',
    # 'crispy_forms',
    #'reversion',
    'clientes',
    'casos',
    #'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'despachoer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],        
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'templates/'),
)

# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Despacho ER',
    'HEADER_DATE_FORMAT': 'l, j F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        'sites',
    #    {'app': 'auth', 'icon':'icon-cog', 'models': ('user', 'group')},
        {'label': 'Control de Acceso', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
        {'label': 'Cliente', 'icon':'icon-question-sign', 'models': ('clientes.cliente', 'clientes.telefono')},
        {'label': 'Catalogos', 'icon':'icon-question-sign', 'models': ('casos.caso', 'casos.etapa')},
        # {'label': 'Cliente', 'icon':'icon-question-sign', 'url': '/admin/clientes/cliente'},
        # {'label': 'Casos', 'icon':'icon-question-sign', 'url': '/admin/casos/caso'},
    #    {'label': 'Cliente', 'icon':'icon-question-s        # {'label': 'Cliente', 'icon':'icon-question-sign', 'url': '/admin/clientes/cliente'},
        # {'label': 'Casos', 'icon':'icon-question-sign', 'url': '/admin/casos/caso'},ign', 'url': '/support/'},
    ),

    # misc
    # 'LIST_PER_PAGE': 15
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt' : "%d/%b/%Y %H:%M:%S"
#         },
#         'tel_verbose': {
#             'format' : "[%(asctime)s] %(levelname)s :: %(message)s",
#             'datefmt' : "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler',
#         },
#         'telefonos': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': 'telefonos.log' if DEBUG else APP_LOGS_DIRECTORY_TEL,
#             'formatter': 'tel_verbose',
#         },
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         # 'personas': {
#         #     'handlers': ['telefonos'],
#         #     'level': 'INFO',
#         # },
#     }
# }

#tweaks
LOGIN_URL = '/admin/'

WSGI_APPLICATION = 'despachoer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'Mexico/General'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static/')

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #os.path.join(PROJECT_PATH, 'static/'),
    '',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Load the local settings
try:
    from local_settings import *
except ImportError:
    print 'No se puede importar local_settings.py'

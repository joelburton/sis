"""
Django settings for turnin project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

from .base import *


INTERNAL_IPS = ["127.0.0.1"]
SECRET_KEY = 'i^ari$22!b+&pwhm=o7h-%vr-%us)#k=q0!g9qcaz*a#!h!k*c'
ALLOWED_HOSTS = ["*"]

DEBUG = True
TEMPLATE_DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar',
)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

##################################################################################################
# Email
#
# We don't want to send real email, so just print to the console


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Joel's MacBook can timeout when at a cafe with incorrectly-set DNS settings, as it doesn't know
# the hostname of the laptop. So let's hack this in:

from django.core.mail.utils import DNS_NAME

DNS_NAME._fqdn = "localhost"

##################################################################################################
# Logging & Error Reporting

# Blather on about every little thing that happens. We programmers get lonely.

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        }

    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

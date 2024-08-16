from .base import * 


# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'django-insecure-g4_@%m_65uy=flaq9m$apz2%ff_d(4b!)0t*(d$dcrylptwdw5'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = []




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


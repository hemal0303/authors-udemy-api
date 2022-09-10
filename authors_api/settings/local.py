# SECURITY WARNING: keep the secret key used in production secret!
from .base import *
from .base import env

DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY", 
    default = 'django-insecure-non&z+bku$39wc&1em%ykpzkq05+1h3o73*%^+11od9zo2zk5h'
    )
# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']
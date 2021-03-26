from .base import *
from decouple import config


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'authdb',
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
    }
}
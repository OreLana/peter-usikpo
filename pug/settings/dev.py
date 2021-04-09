from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pugdb',
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
    }
}
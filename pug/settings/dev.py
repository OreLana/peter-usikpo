from .base import *
from decouple import config

SECRET_KEY = 'm^c4nk2=pj@8c)a@vmqxbzqd20@xp4kr)k(_^)qwyqckl8g9&4'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'authdb',
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
    }
}
from .base import *


#Github Action environment variables
SECRET_KEY = 'm^c4nk2=pj@8c)a@vmqxbzqd20@xp4kr)k(_^)qwyqckl8g9&4'
DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'github_actions',
    'USER': 'postgres',
    'PASSWORD': 'postgres',
    'HOST': '127.0.0.1',
    'PORT': '5432',
    }
}
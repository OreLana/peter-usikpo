from decouple import config

ENVIRONMENT = config('ENVIRONMENT')
if ENVIRONMENT == 'development':
    from .dev import *
elif ENVIRONMENT == 'production':
    from .production import *


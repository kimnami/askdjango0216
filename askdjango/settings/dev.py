from .common import *

INSTALLED_APP+=['debug_toolbar']
MIDDLEWARE = += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ['127.0.0.1']

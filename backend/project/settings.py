import os
import sys

from corsheaders.defaults import default_headers

try:
    from settings_local import *
except ImportError:
    pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.abspath(os.path.join(PROJECT_DIR, '..'))
PUBLIC_DIR = os.path.abspath(os.path.join(PARENT_DIR, '../../public'))

sys.path.insert(0, os.path.abspath(os.path.join(PARENT_DIR, 'libs')))

SECRET_KEY = '(pmk9(b79_pu=9bxa1ii^*r3kpy75-q(@rcye*#un)6hyfuj17'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(PUBLIC_DIR, 'media')
STATIC_ROOT = os.path.join(PUBLIC_DIR, 'static')

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'tastypie',
    'django_extensions',
    'annoying',
    'corsheaders',

    'users',
    'core',
]


########################
##  PROJECT SETTINGS  ##
########################

# DJANGO
AUTH_USER_MODEL = 'users.User'
USER_HANDLE_LIMIT = 4
APPEND_SLASH = False

# CELERY
CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'

# DJANGO-CORS-HEADERS
if DEBUG:
    CORS_ORIGIN_ALLOW_ALL = True

else:
    CORS_ORIGIN_WHITELIST = ('devdb.io',)

# BLEACH
HTML_ALLOWED_TAGS = [
    'p', 'strong', 'em',
    's', 'sub', 'sup',
    'ul', 'ol', 'li',
]

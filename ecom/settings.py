import os
import tempfile
import sys
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# Load environment variables from .env file
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = load_dotenv(os.path.join(BASE_DIR, '.env'))
load_dotenv(env_path)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-euj+yr-b+425m3te#y34-mj*4l6%va^i9#2krzjr3o1aljjvg&')

# Determine if the environment is production, development, or testing
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'
ALLOWED_HOSTS = ['ahmedelasmai.eu.pythonanywhere.com'] if not DEBUG else []
CSRF_TRUSTED_ORIGINS = ['https://ahmedelasmai.eu.pythonanywhere.com'] if not DEBUG else []

# Application definition
INSTALLED_APPS = [
    'cart',
    'user',
    'products',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecom.urls'

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

WSGI_APPLICATION = 'ecom.wsgi.application'

# Database configuration
AUTH_USER_MODEL = 'user.User'

if 'test' in sys.argv:
    # Use an in-memory SQLite database for tests
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
else:
    if 'DATABASE_URL' in os.environ and not DEBUG:
        DATABASES = {
            'default': dj_database_url.config(
                conn_max_age=500,
                conn_health_checks=True,
            )
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static and Media files
STATIC_URL = '/static/'
MEDIA_URL = '/mediafiles/' if not DEBUG else '/media/'

if 'test' in sys.argv:
    # Use a temporary directory for media files during tests
    TEMP_MEDIA = tempfile.TemporaryDirectory()
    MEDIA_ROOT = TEMP_MEDIA.name
else:
    if not DEBUG:
        STATIC_ROOT = '/home/ahmedelasmai/ahmedelasmai.eu.pythonanywhere.com/staticfiles'
        MEDIA_ROOT = '/home/ahmedelasmai/ahmedelasmai.eu.pythonanywhere.com/mediafiles'
    else:
        STATICFILES_DIRS = [BASE_DIR / 'ecom/static']
        MEDIA_ROOT = BASE_DIR / 'media'

# Authentication redirects
LOGIN_REDIRECT_URL = '/products'
LOGIN_URL = '/user/login'
LOGOUT_REDIRECT_URL = '/user/login'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

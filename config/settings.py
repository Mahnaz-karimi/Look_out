"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import json
import os
from pathlib import Path
import django_heroku
import dj_database_url

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

if os.path.exists('/etc/blog.json'):
    with open('/etc/blog.json') as config_file:
        config = json.load(config_file)
        SECRET_KEY = config.get('SECRET_KEY')
        AWS_ACCESS_KEY_ID = config.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = config.get('AWS_SECRET_ACCESS_KEY')
        AWS_STORAGE_BUCKET_NAME = config.get('AWS_STORAGE_BUCKET_NAME')
        DEBUG = (config.get('DEBUG_VALUE') == 'True')
        ALLOWED_HOSTS = config.get('ALLOWED_HOSTS')
        EMAIL_HOST_USER = config.get('EMAIL_USER')
        EMAIL_HOST_PASSWORD = config.get('EMAIL_PASS')
        DATABASES = {
            'default': {
                'ENGINE': config.get('DB_ENGINE'),
                'NAME': config.get('DB_NAME'),
                'USER': config.get('DB_USER'),
                'PASSWORD': config.get('DB_PASSWORD'),
                'HOST': config.get('DB_HOST'),
                'PORT': config.get('DB_PORT'),
            }
        }
else:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    DEBUG = os.environ.get('DEBUG_VALUE')
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')
    EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
    DATABASES = {}
    if 'DYNO' in os.environ:  # Dette sker kun på Heroku, hvis man er på heroku så skal dette settes op
        DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.environ.get('DB_NAME'),
                'USER': os.environ.get('DB_USER'),
                'PASSWORD': os.environ.get('DB_PASSWORD'),
                'HOST': os.environ.get('DB_HOST'),
                'PORT': os.environ.get('DB_PORT'),
            }
        }

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'person.apps.PersonConfig',
    'crispy_forms',
    'storages',  # AWS
    'embed_video',
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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_URL = '/static/'
STATIC_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'pictures')
MEDIA_URL = '/pictures/'

django_heroku.settings(locals())
CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog:blog-home'
LOGIN_URL = 'person:login'

PAGINATION_COUNT = 12


FEATURES = {}
if os.path.exists('/etc/features.json'):
    with open('/etc/features.json') as feature_file:
        FEATURES = json.load(feature_file)
elif 'FEATURES' in os.environ:
    FEATURES = json.loads(os.environ.get('FEATURES'))

# AWS
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

region_name = 'AWS_S3_REGION_NAME'
AWS_S3_REGION_NAME = 'eu-central-1'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# Send a mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
if os.path.exists('/etc/blog.json'):
    with open('/etc/blog.json') as config_file:
        EMAIL_HOST_USER = config.get('EMAIL_HOST_USER')
        EMAIL_HOST_PASSWORD = config.get('EMAIL_HOST_PASSWORD')

else:
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
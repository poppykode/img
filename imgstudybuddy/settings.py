"""
Django settings for imgstudybuddy project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from django.contrib.messages import constants as messages
from environs import Env

env = Env()
env.read_env()


MESSAGE_TAGS = {
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.ERROR: 'danger',
    messages.WARNING: 'warning',
}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = Path(BASE_DIR/ 'static_files')
TEMPLATE_DIR = Path(BASE_DIR/ 'templates')
MEDIA_DIR = Path(BASE_DIR/ 'media')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4o&cl$xacf_&_f0=m(ja8i5&0p#qh@e0qg%-3e)$3l2u_0mcal'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Custom Apps
    'core',
    'accounts',
    'stations',
    'subscriptions',
    'meeting_calendar',
    'offers',
    'review_ratings',
    'study_buddies',
    'coaches',
    #3rd Part Apps
    'crispy_forms',
    'crispy_bootstrap5',
    'django_crontab',


]
APP_BASE_URL = 'http://127.0.0.1:8000'

CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRONJOBS = [
    
    ('*/2 * * * *', 'subscriptions.utils.meetings_due_for_check_in'),
    ('*/2.30 * * * *', 'subscriptions.utils.meetings_due_for_check_out'),
    ('0 0 * * *', 'subscriptions.utils.expire_subscriptions'),
]

# CKEDITOR_5_CONFIGS = {
#     'extends': {
#         'toolbar': ['heading','|', 'bold','|', 'italic','|', 'underline','|',
#                     'bulletedList','|', 'numberedList','|', 'blockQuote','|',
#                     'paragraph',],
#     },
# }

# TINYMCE_DEFAULT_CONFIG = {
#     'selector': 'textarea',
#     'plugins': 'advlist autolink lists link image charmap print preview anchor',
#     'toolbar': 'undo redo | styleselect | bold italic | alignleft aligncenter alignright | bullist numlist outdent indent | link image',
# }


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'imgstudybuddy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'imgstudybuddy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'img_db',
        'USER': 'root',
        'PASSWORD': 'root2',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
BASE_URL = 'http://77.37.122.93'


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = 'accounts/q/login'

AUTH_USER_MODEL = 'accounts.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR, ]
STATIC_ROOT = Path(BASE_DIR/ 'static')
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'expresscareweb@gmail.com'
SERVER_EMAIL = 'expresscareweb@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'expresscareweb@gmail.com'
EMAIL_HOST_PASSWORD = 'lqpa hghx srex sjyv'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# EMAIL_USER = 'no-reply@imgstudybuddy.com'
# TO_ = 'no-reply@imgstudybuddy.com'
# PASSWORD = 'I1m1@1n1i1d1o1n1d1o1'
# SMTP ='smtp.privateemail.com'
# PORT =  465
# DEFAULT_FROM_EMAIL = EMAIL_USER

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.privateemail.com'  # Replace with your Namecheap server address
# EMAIL_PORT = 465  # Or 587 depending on your Namecheap configuration
# EMAIL_USE_TLS = True  # Or EMAIL_USE_SSL = True if required
# EMAIL_HOST_USER = 'no-reply@imgstudybuddy.com'  # Replace with your Namecheap email address
# EMAIL_HOST_PASSWORD = 'I1m1@1n1i1d1o1n1d1o1'  # Replace with your secure password
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # Optional, customize sender name


try:
    from .local_settings import *
except:
    pass


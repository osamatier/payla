"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 2.2.28.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "93sl4j#(bqz_266(4m)p+v4pr=-@w^to71(@$1r%ov1**=2o^w"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["0.0.0.0"]
PORT = 8000
BASE_URL = f"http://0.0.0.0:{PORT}"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "core.apps.CoreConfig",
    "newsletter.apps.NewsletterConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "server.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_NAME"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": "db",
        "PORT": 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # Noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # Noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # Noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # Noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = "localhost"
EMAIL_PORT = 25
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "support@newsletter.de"
EMAIL_HOST_PASSWORD = ""

# newsletter
NEWSLETTER_EMAIL_BATCH_SIZE = 2  # for test
NEWSLETTER_EMAIL_SUBJECT = "Your Newsletter - Enjoy it!"
NEWSLETTER_EMAIL_EMAIL_TEMPLATE = "newsletter/newsletter.txt"
CONFIRMATION_LINK_VALIDITY_HOURS = 6
SUBSCRIPTION_CONFIRMATION_EMAIL_SUBJECT = "One step to complete the subscription"
SUBSCRIPTION_CONFIRMATION_EMAIL_TEMPLATE = "newsletter/subscription_confirm.txt"

# Auth
AUTH_USER_MODEL = "core.User"

# DRF
# https://www.django-rest-framework.org/

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "EXCEPTION_HANDLER": "core.exceptions.api_exception_handler",
    "DATETIME_FORMAT": ("%Y-%m-%dT%H:%M:%S"),
}

# Djoser
# https://djoser.readthedocs.io/en/latest/introduction.html

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
}  # Noqa

DJOSER = {
    "SERIALIZERS": {"user_create": "core.serializers.UserCreateSerializer"}
}  # Noqa

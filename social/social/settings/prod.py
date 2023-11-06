from .base import *
from .config import DB_NAME, DB_PASS, DB_USER, DB_HOST, DB_PORT

DEBUG = False
EMAIL_PROTOCOL = 'http'  # To alter
EMAIL_DOMAIN = 'localhost:3000'  # To alter

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

ALLOWED_HOSTS = ['*']
CORS_ALLOWED_HEADERS = ['*']
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'SET_USERNAME_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_URL': r'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': r'email/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': r'activate/{uid}/{token}',
    'SOCIAL_AUTH_TOKEN_STRATEGY': 'djoser.social.token.jwt.TokenStrategy',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {
        'user_create': 'apps.accounts.api.v1.serializers.MyUserCreateSerializer',
        'user': 'apps.accounts.api.v1.serializers.MyUserCreateSerializer',
        'current_user': 'apps.accounts.api.v1.serializers.MyUserCreateSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },
    'EMAIL': {
        'activation': 'social.email.MyActivationEmail',
        'html': True
    },
    # Coming Soon
    # 'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': ['http://127.0.0.1:8000/'],
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}


import os

from celery.schedules import crontab

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = os.environ['SERVER'] == 'dev'

if DEBUG is False:
    ALLOWED_HOSTS = [
        '127.0.0.1:8000',
        '*',
    ]

if DEBUG is True:
    ALLOWED_HOSTS = [
        '127.0.0.1:8000',
        '*',
    ]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rate',
    'django_extensions',
    'debug_toolbar',
    'account',
    'rest_framework',
    'drf_yasg',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'currency.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'currency.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': 'postgres',
        'PORT': '5432',
    }
}
# CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': '172.18.0.2:11211',
#    }
# }

# REDIS_HOST = 'redis'

REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
REDIS_CACHE_LOCATION = os.environ['REDIS_CACHE_LOCATION']
REDIS_URI = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/"

CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": REDIS_URI + REDIS_CACHE_LOCATION,
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'account.User'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join('/tmp', 'static_content', 'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_content')

# CELERY_BROKER_URL = 'amqp://localhost'
# Celery
CELERY_BROKER_URL = 'amqp://{0}:{1}@rabbitmq:5672//'.format(
    os.environ.get('RABBITMQ_DEFAULT_USER', 'guest'),
    os.environ.get('RABBITMQ_DEFAULT_PASS', 'guest'),
)

CELERY_BEAT_SCHEDULE = {
    'parse': {
        'task': 'rate.tasks.parse_privatbank',
        'schedule': crontab(minute='*/5'),
    },
    'parse_mb': {
        'task': 'rate.tasks.parse_monobank',
        'schedule': crontab(minute='*/5'),
    },
    'parse_m': {
        'task': 'rate.tasks.parse_minora',
        'schedule': crontab(minute='*/5'),
    },
    'parse_p': {
        'task': 'rate.tasks.parse_pumb',
        'schedule': crontab(minute='*/5'),
    },
    'parse_kb': {
        'task': 'rate.tasks.parse_kredobank',
        'schedule': crontab(minute='*/5'),
    },
}

INTERNAL_IPS = [

    '127.0.0.1',
]

# sending email
EMAIL_HOST_USER = 'lbdltest77@gmail.com'
EMAIL_HOST_PASSWORD = 'django77'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'example@ex.com'
    DOMAIN = 'http://127.0.0.1:8000'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

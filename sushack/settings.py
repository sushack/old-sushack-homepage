# Django settings for sushack project.
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
import dj_database_url


DIRNAME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

DEBUG = bool(os.environ.get('DEBUG', False))
DEVELOPMENT_SITE = bool(os.environ.get('DEVELOPMENT_SITE', False))

DATABASES = {'default': dj_database_url.config(default='postgres://localhost/sushack')}

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'www.sushack.co.uk', 'sushack.herokuapp.com']

ADMINS = (('Admin', 'hello@sushack.co.uk'), ('max', 'moglenstar@gmail.com'), )
MANAGERS = ADMINS
ADMIN_EMAILS = zip(*ADMINS)[1]
EMAIL_SUBJECT_PREFIX = '[sushack] '
SERVER_EMAIL = DEFAULT_FROM_EMAIL = 'hello@sushack.co.uk'
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')

TIME_ZONE = 'UTC'
USE_L10N = True  # Locale
USE_TZ = True

LANGUAGE_CODE = 'en-GB'
USE_I18N = False  # Internationalization

# AWS
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_LOCATION = os.environ.get('AWS_LOCATION', '')
AWS_S3_SECURE_URLS = False
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', 'refresh-oxford')
AWS_S3_CUSTOM_DOMAIN = os.environ.get('AWS_S3_CUSTOM_DOMAIN')
AWS_CLOUDFRONT_STREAMING_DOMAIN = os.environ.get('AWS_CLOUDFRONT_STREAMING_DOMAIN')
DEFAULT_FILE_STORAGE = os.environ.get('DEFAULT_FILE_STORAGE', 'queued_storage.backends.QueuedS3BotoStorage')
STATICFILES_STORAGE = os.environ.get('STATICFILES_STORAGE', 'incuna_storages.backends.S3StaticStorage')
S3_URL = 'http://{0}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)

# Static
MEDIA_ROOT = os.path.join(DIRNAME, 'client_media')
MEDIA_URL = '/client_media/'
STATIC_ROOT = os.path.join(DIRNAME, 'static_media')
STATIC_URL = os.environ.get('STATIC_URL', S3_URL + 'static/')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DEBUG = DEBUG
TEMPLATE_DIRS = (os.path.join(DIRNAME, 'templates'))
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'admin_sso.auth.DjangoSSOAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'sushack.urls'
SECRET_KEY = '$$g6*tl!&amp;u4kd9!cs*re9#-u+xe!)25)m0(&amp;*1%8k*p*&amp;^cc6i'
SITE_ID = 1
WSGI_APPLICATION = 'sushack.wsgi.application'

INSTALLED_APPS = (
    # Project Apps
    'sushack',

    # Libraries
    'admin_sso',
    'crispy_forms',
    'south',
    'debug_toolbar',
    'django_extensions',
    'feincms',
    'feincms.module.page',
    'gravatar',
    'gunicorn',
    'raven.contrib.django',

    # Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

SENTRY_DSN = os.environ.get('SENTRY_DSN')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '[%(asctime)s][%(levelname)s] %(name)s %(filename)s:%(funcName)s:%(lineno)d | %(message)s',
            'datefmt': '%H:%M:%S',
        },
    },
    'filters': {
        'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'}
    },
    'handlers': {
        'sentry': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'raven.contrib.django.handlers.SentryHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['sentry', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'incuna.default': {
            'handlers': ['sentry', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'sentry.errors': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propogate': True,
        },
    }
}

# Debug Toolbar
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
INTERNAL_IPS = ('127.0.0.1',)

# FeinCMS
FEINCMS_RICHTEXT_INIT_CONTEXT = {
    'TINYMCE_JS_URL': STATIC_URL + 'scripts/tiny_mce/tiny_mce.js',
}

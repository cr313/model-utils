import os

INSTALLED_APPS = (
    'model_utils',
    'tests',
)

if os.environ.get('SQLITE'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        },
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("DB_NAME", "modelutils"),
            "USER": os.environ.get("DB_USER", 'postgres'),
            "PASSWORD": os.environ.get("DB_PASSWORD", ""),
            "HOST": os.environ.get("DB_HOST", "localhost"),
            "PORT": os.environ.get("DB_PORT", 5432)
        },
    }

SECRET_KEY = 'dummy'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

USE_TZ = True

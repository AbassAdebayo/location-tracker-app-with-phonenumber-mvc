import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Security settings
SECRET_KEY = 'your-secret-key'
# ABSTRACT_API_KEY = ''
# OPENCAGE_API_KEY = ''
# IPINFO_API_TOKEN = ''
# TWILIO_ACCOUNT_SID = ''
# TWILIO_AUTH_TOKEN = ''

IPINFO_API_TOKEN = os.getenv('IPINFO_API_TOKEN')
ABSTRACT_API_KEY = os.getenv('ABSTRACT_API_KEY')

DEBUG = True  # Set to False in production
ALLOWED_HOSTS = [
    'your-vercel-domain.vercel.app',
    '127.0.0.1',
    'localhost',
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'USERS',
    'LOCATION',
    'channels',
    'rest_framework'
]

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}



# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

SESSION_COOKIE_AGE = 3600  # 1 hour

X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Set the session to expire on browser close
SESSION_SAVE_EVERY_REQUEST = True

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# Database configuration
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'location_tracking_db',
#         'USER': 'track_app_user',
#         'PASSWORD': 'DefinedCode',
#         'HOST': 'localhost',  
#         'PORT': '3306', 
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
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
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# WSGI application
WSGI_APPLICATION = 'LOCATION_TRACKING_APP.wsgi.application'
ASGI_APPLICATION = 'LOCATION_TRACKING_APP.asgi.application'

ROOT_URLCONF = 'LOCATION_TRACKING_APP.urls'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication settings
AUTH_USER_MODEL = 'USERS.CustomUser'
LOGIN_REDIRECT_URL = 'track'
LOGOUT_REDIRECT_URL = 'login'

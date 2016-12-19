import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for magic project.

Generated by 'django-admin startproject' using Django 1.8.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=gujasv1o=s%7gkjp@+ue^zv%t%w#_g)ts36hneplw5xkceci*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

ROOT_URLCONF = 'magic.urls'

WSGI_APPLICATION = 'magic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/New_York'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'magic', 'static'),
)
SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'magic', 'templates'), ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.debug',
                'django.core.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.csrf',
                'django.core.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.core.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]


MIDDLEWARE_CLASSES = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
]

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_column',
    'djangocms_file',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'reversion',

    'aldryn_bootstrap3',
    'filer',
    'easy_thumbnails',
    'aldryn_style',

    'smart_mirror_clock',
    'smart_mirror_weather',
    'magic'
]

LANGUAGES = (
    # Customize this
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    # Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    # Customize this
    ('fullwidth.html', 'Fullwidth'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

MIGRATION_MODULES = {
    
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

ALDRYN_STYLE_CLASS_NAMES = (
    ('container', gettext('container')),
    ('container-fluid', gettext('container-fluid')),
)

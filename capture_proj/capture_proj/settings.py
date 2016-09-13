#coding:utf-8
"""
Django settings for capture_proj project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2-a6$lsgixpci^x@ndenyt9*bxpjq+sufu5yl+sg+!o+t202_*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'capture_proj.urls'

WSGI_APPLICATION = 'capture_proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

#--------------------------------
SOURCE_URL = '***'
LOGIN_URL = SOURCE_URL+'login'

USERNAME = '**'
PASSWORD = '**'

PICTURE_DIR = os.path.join(BASE_DIR, 'static/dj')

TARGET_URL = [
    {u'数据库服务器': SOURCE_URL+'dashboard/db/2-1-xi-tong-jian-kong-shu-ju-ku-fu-wu-qi'},
    {u'防火墙': SOURCE_URL+'dashboard/db/1-1-wang-luo-she-bei-fang-huo-qiang'},
    {u'应用服务器': SOURCE_URL+'dashboard/db/2-2xi-tong-jian-kong-ying-yong-fu-wu-qi'},
    {u'数据库监控': SOURCE_URL+'dashboard/db/3-shu-ju-ku-jian-kong'},
    {u'es': SOURCE_URL+'dashboard/db/4-es'},
    {u'外部接口': SOURCE_URL+'dashboard/db/5-wai-bu-jie-kou'},
    {u'典型业务': SOURCE_URL+'dashboard/db/6-dian-xing-ye-wu'},
    {u'mq': SOURCE_URL+'dashboard/db/7-rabbitmq-jian-kong'},
]

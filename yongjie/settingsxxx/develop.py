import os
from .default import *

SECRET_KEY = 'v^qtma$#$)&xb$%du7b+_4x373o&#vb8tw8o0#1s)0_6ta(mx8'

DEBUG = True


ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
	'home',
    'news',
    'mobile',
]
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# 设置每页显示数量
DOMAIN_NAME='http://localhost:8000'
EACH_PAGE_BLOGS_NUMBER=3
EACH_PAGE_SOLUTIONS_NUMBER=4





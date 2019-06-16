import os
from .default import *

SECRET_KEY = 'v^qtma$#$)&xb$%du7b+_4x373o&#vb8tw8o0#1s)0_6ta(mx8'

DEBUG = False

#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['localhost','127.0.0.1','47.94.235.194']

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


#DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'shunshang_db',         # 你要存储数据的库名，事先要创建之
        'USER': 'sunsang',         # 数据库用户名
        'PASSWORD': 'Ss390219@sub26',     # 密码
        'HOST': '47.94.235.194',    # 主机
        'PORT': '3306',         # 数据库使用的端口
    }
}




# 设置每页显示数量
DOMAIN_NAME='http://localhost:8000'
EACH_PAGE_BLOGS_NUMBER=3
EACH_PAGE_SOLUTIONS_NUMBER=4




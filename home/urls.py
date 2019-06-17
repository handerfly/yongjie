"""yongjie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='home'),
    path('solution', views.solution, name='solution'),
    path('solution_detail/<int:solution_id>', views.solution_detail, name='solution_detail'),
    path('lab', views.lab, name='lab'),

    path('cases/<int:type>', views.cases, name='cases'),
    path('case_detail/<int:case_id>', views.case_detail, name='case_detail'),

    path('service', views.service, name='service'),

    path('products/<int:type>/<str:sub_type>', views.products, name='products'),
    path('product_detail/<int:product_id>', views.product_detail, name='product_detail'),

    path('news/<int:type>', views.news, name='news'),
    path('news_detail/<int:news_id>', views.news_detail, name='news_detail'),

    path('about/<int:about_id>', views.about, name='about'),
    path('honer', views.honer, name="honer"),

    path('price', views.price, name="price")


]

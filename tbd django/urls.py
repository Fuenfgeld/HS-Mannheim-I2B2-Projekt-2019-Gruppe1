"""tbd_django_javascript URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import tbdApp.views

urlpatterns = [
    url(r'^$', tbdApp.views.index, name = 'index'),
    url(r'age$', tbdApp.views.age, name = 'age'),
    url(r'^race$', tbdApp.views.race, name = 'race'),
    url(r'^sex$', tbdApp.views.sex, name = 'sex')
]

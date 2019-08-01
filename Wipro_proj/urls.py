"""Wipro_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
#from accounts import views as accounts_views
from Wipro_app import views
from django.urls import path, include
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login,name='login'),
    path('Profile/', views.Profile,name='Profile'),
    path('MyHistory/', views.MyHistory,name='MyHistory'),
    path('ColleagueHistory/', views.ColleagueHistory,name='ColleagueHistory'),
    path('home/', views.home,name='home'),
    path('AddOrg/', views.AddOrg,name='AddOrg'),
	path('ForgetPassword/', views.ForgetPassword,name='ForgetPassword'),
	path('add_category/', views.add_category,name='add_category'),
	path('add_question/', views.add_question,name='add_question'),
    path('change_password/', views.change_password,name='change_password'),
    path('Assessment/', views.assessment,name='Assessment'),
	path('assessment_from_db/', views.assessment,name='assessment_from_db'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
]




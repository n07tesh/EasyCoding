"""EasyCoding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home. name='home'as_view(),)
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

admin.site.site_header = "EasyCoding Admin"
admin.site.site_title = "EasyCoding Admin Panel"
admin.site.index_title = "Welcome To EasyCoding Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls')),
    path('blog/',include('Blog.urls')),
    path('tinymce/', include('tinymce.urls')),
]
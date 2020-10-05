from django.contrib import admin
from django.urls import path, include
from .import views

app_name = 'Blog'

urlpatterns = [
    path('',views.BlogHome,name='BlogHome'),
    path('<str:slug>',views.BlogPost,name='BlogPost')
]
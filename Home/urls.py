from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'Home'

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('contact/', views.Contact, name='Contact'),
    path('about/',views.AboutView.as_view(),name='about'),
]
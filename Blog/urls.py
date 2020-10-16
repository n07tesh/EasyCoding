from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('postComment',views.postComment,name="postComment"),
    path('',views.BlogHome,name='BlogHome'),
    path('<str:slug>',views.BlogPost,name='BlogPost'),

]
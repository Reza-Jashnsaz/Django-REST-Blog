
from django.contrib import admin
from django.urls import path,include
from . import views


#home urls
urlpatterns = [
    # api/v1/posts/
    path('posts/', views.posts , name='posts'),
    path('posts/<id>/', views.post , name='post'),
    path('posts/create/', views.create_post , name='create_post'),
    path('posts/update/<id>/', views.update_post , name='update_post'),
    path('posts/delete/<id>/', views.delete_post , name='delete_post'),
]
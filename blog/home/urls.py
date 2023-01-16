
from django.contrib import admin
from django.urls import path,include
from . import views


#home urls
urlpatterns = [
    path('', views.home , name='home'),
    path('post/<id>', views.post , name='post'),
    path('posts/create', views.create_post , name='create_post'),
    path('posts/edit/<id>', views.edit_post , name='edit_post'),
    path('posts/update/<id>', views.update_post , name='update_post'),
    path('posts/delete/<id>', views.delete_post , name='delete_post'),
    path('comments/create/<post_id>', views.create_comment , name='create_comment'),
]
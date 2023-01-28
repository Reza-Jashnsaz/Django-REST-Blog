from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title' , 'text' , 'created_at']
    list_filter = ['created_at']
    search_fields = ('title' , 'text' , 'created_at')
    # for slug ===> prepopulated_fields = {'slug' : ('title')}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id' , 'text']


admin.site.register(Post , PostAdmin)
admin.site.register(Comment , CommentAdmin)
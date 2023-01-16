from django.shortcuts import render , redirect
from home.models import Post,Comment
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from django.contrib import messages
from .forms import PostForm,CommentForm


#posts list
def home(request):
    posts = Post.objects.order_by('-id')
    return render(request, 'home.html' ,{'posts':posts})


#single post
def post(request , id):
    post = Post.objects.get(id = id)
    comments = Comment.objects.filter(post_id = id).order_by('-id')
    return render(request, 'single.html' ,{'post':post , 'comments':comments})



#create new post
def create_post(request):
    #validation first
    form = PostForm(request.POST)
    if form.is_valid():
        Post.objects.create(
            title = request.POST.get('title'),
            text = request.POST.get('text'),
            created_at = datetime.now()
        )
        messages.success(request, 'post created')
        return redirect('home')
    else:
        messages.error(request, 'validation failed')
        return redirect('home')
    


#edit post page
def edit_post(request , id):
    post = Post.objects.get(id = id)
    return render(request , 'edit.html' , {'post':post})



#update post query
def update_post(request , id):
    #validation first
    form = PostForm(request.POST)
    if form.is_valid():
        Post.objects.filter(id=id).update(
            title = request.POST.get('title'),
            text = request.POST.get('text'),
        )
        messages.success(request, 'post updated')
        return redirect('home')
    else:
        messages.error(request, 'validation failed')
        return redirect('home')
    


#delete post
def delete_post(request , id):
    Post.objects.get(id = id).delete()
    messages.success(request, 'post deleted')
    return redirect('home')




#create comment for a post
def create_comment(request , post_id):
    #validation first
    form = CommentForm(request.POST)
    if form.is_valid():
        Comment.objects.create(
            text = request.POST.get('text'),
            post_id = Post.objects.get(id = post_id)
        )
        messages.success(request, 'comment created')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        messages.error(request, 'validation failed')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    
    

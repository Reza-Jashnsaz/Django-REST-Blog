from django.shortcuts import render , redirect 
from home.models import Post,Comment
from datetime import datetime
from .serializers import *
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes



        
        
        
#posts list
@api_view(['GET'])
def posts(request):
    posts = Post.objects.order_by('-id')
    posts = PostSerializer(posts , many = True).data
    return Response({
        'message' : "success", 
        'data': posts,
    }, status = 200)
    


#single post
@api_view(['GET'])
def post(request , id):
    post = Post.objects.get(id = id)
    comments = Comment.objects.filter(post_id = id).order_by('-id')
    post = PostSerializer(post).data
    comments = CommentSerializer(comments , many = True).data
    return Response({
        'message' : "success", 
        'data': [post, comments],
    }, status = 200)





#create new post
@api_view(['POST'])
def create_post(request):
    
    #validation first
    serializer = PostSerializer(data = request.POST)
    if serializer.is_valid():
        Post.objects.create(
            title = request.POST.get('title'),
            text = request.POST.get('text'),
        )
        return Response({
            'message' : "success", 
        }, status = 200)

    else:
         return Response({
            'message' : "error", 
            'data' : serializer.errors
        }, status = 400)
  





#update post 
@api_view(['PUT'])
def update_post(request , id):
    
    #validation first
    serializer = PostSerializer(data = request.POST )
    if serializer.is_valid():
        Post.objects.filter(id=id).update(
            title = request.POST.get('title'),
            text = request.POST.get('text'),
        ) 
        return Response({
            'message' : "success", 
        }, status = 200)

    else:
         return Response({
            'message' : "error", 
            'data' : serializer.errors
        }, status = 400)
  





#delete post
@api_view(['DELETE'])
def delete_post(request , id):
    Post.objects.get(id = id).delete()
    return Response({
        'message' : "success", 
    }, status = 200)





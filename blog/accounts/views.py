from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


#signup user
@api_view(['POST'])
def user_register(request):
    
    #validation first
	serializer = RegisterSerializer(data = request.POST)
	if serializer.is_valid():
		User.objects.create_user(request.POST.get('username'),request.POST.get('email'),request.POST.get('password'))
		return Response({
			"message" : "success",
			"data" : serializer.data,
        } , status = 200)
	
	else:
		return Response({
			'message' : "error", 
			'data' : serializer.errors
		}, status = 400)
  
    




#signin user
@api_view(['POST'])
def user_login(request):
	
	#validation
	serializer = LoginSerializer(data = request.POST)
	if serializer.is_valid():
		sd = serializer.data
		user = authenticate(request, username=sd['username'], password=sd['password'])
		if user is not None:
        #correct username password
			login(request, user)
			token = Token.objects.create(user=user)
			return Response({
				"message" : "success",
				"data" : [serializer.data , token.key],
			} , status = 200)	
		else:
        #wrong username or password
			return Response({
				"message" : "username or password is wrong",
			} , status = 400)
	
	#if serializer is not valid
	return Response({
			'message' : "error", 
			'data' : serializer.errors
		}, status = 400)
  




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    #delete token and logout user
	Token.objects.get(key = request.user.auth_token).delete()
	logout(request)
	return Response({
		"message" : "success",
	} , status = 200)
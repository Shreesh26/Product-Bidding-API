from django.shortcuts import render
from django.contrib.auth.models import User
from numpy import roll
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *

class SignUp (APIView):
    @staticmethod
    def post(request):
        username=request.data['un']
        email=request.data['email']
        fname=request.data['fn']
        lname=request.data['ln']
        pw=request.data['pass']
        cpw=request.data['cpass']

        if len(username)<4:
            return Response("Your Username cannot be less than 4 characters")
        if (pw!=cpw):
            return Response("Passwords do not match")
        

        try:
            new_usr=User.objects.get(username=username)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            new_usr = None
        
        
        if new_usr is None:
            user=User.objects.create_user(username,email,pw)
            user.first_name=fname
            user.last_name=lname
            user.save()
            return Response("Account Created")
        else:
            return Response("Username already exists, Try a different Username")

class UserProfile(APIView):
    @staticmethod
    def get(request):
        user=request.user
        user_data=list(UserDetail.objects.filter(user=user).values())
        return Response(user_data)

    def post(request):
        data=request.data
        user=data["user"]
        roll_number=data["roll_number"]
        name=data['name']
        img=data["img"]
        usr_data=UserDetail(user=user, img=img, roll_number=roll_number, name=name)
        usr_data.save()
        return Response("Details updated successfully")

class ViewUser(APIView):
    @staticmethod
    def get(request):
        un=request.data["un"]
        user=User.objects.filter(username=un)[0]
        print(un)
        usr_detail=list(UserDetail.objects.filter(user=user).values())
        return Response(usr_detail)
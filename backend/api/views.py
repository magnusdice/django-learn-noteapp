from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() #list of objects when creating a new user
    serializer_class = User # what kinda of data that it accepts
    permission_classes = [AllowAny] #who can actually call it anyone or specifics
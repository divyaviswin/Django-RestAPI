from django.contrib import messages
from .models import Pet
from .serializers import PetSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PetList(generics.ListCreateAPIView):
    #queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
    	if self.request.user.is_authenticated() :
    		return Pet.objects.filter(owner=self.request.user)
    	else:
    		return Pet.objects.all()

    def perform_create(self, serializer):
    	Pet.objects.filter(owner=self.request.user)
    	serializer.save(owner=self.request.user)

class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
    	
    	if self.request.user.is_authenticated() :
    		return Pet.objects.filter(owner=self.request.user)
    	else:
    		return Pet.objects.all()







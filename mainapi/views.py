from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,parser_classes
from rest_framework.parsers import FormParser
from rest_framework.response import Response
from .models import Pet
from django.http import HttpResponse
from .serializers import PetSerializer
from django.contrib.auth.models import User




@api_view(('GET','POST'))
@parser_classes((FormParser,))
#@renderer_classes((BrowsableAPIRenderer,))
def pet_list(request):
    if request.method == 'GET':
        user=User.objects.get(id=request.user.id)
        pets=Pet.objects.filter(owner=user)
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)

@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes((FormParser,))
def pet_user(request,pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        user=User.objects.get(id=request.user.id)
        all_pets=Pet.objects.filter(owner=user)
        pet=all_pets.filter(pk=pk)
    except Pet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PetSerializer(pet,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = PetSerializer(pet, data=request.data)

        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':

        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def dashboard(request):
    return HttpResponse("Welcome")


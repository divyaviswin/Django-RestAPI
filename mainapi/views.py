from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pet
from django.http import HttpResponse
from .serializers import PetSerializer




@api_view(('GET','POST'))
def pet_list(request):
    if request.method == 'GET':
        pets=Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)

@api_view(['GET', 'PUT', 'DELETE'])
def pet_user(request):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        pets = Pet.objects.get(owner=request.user)
    except Pet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PetSerializer(pets)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = PetSerializer(pets, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':

        pets.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

def dashboard(request):
    return HttpResponse("Welcome")


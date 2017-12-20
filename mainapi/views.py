from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Pet

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login

from .serializers import PetSerializer
from django.http import JsonResponse



@api_view(('GET','POST'))
def pet_list(request):
    if request.method == 'GET':
        pets=Pet.objects.filter(owner=request.user)
        serializer = PetSerializer(pets, many=True)
        return JsonResponse({"models_to_return": list(serializer)})

        #return Response(serializer)

    elif request.method=='POST':
        serializer=PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)

def dashboard(request):
    #return JsonResponse({"hello":"divya"})
    return HttpResponse("Welcome")


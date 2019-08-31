from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def hello_world(request):
    return Response({"message": "hello world"})

@api_view(["GET"])
def hello_frey(request):
    return Response({"message": "hello frey !!"})
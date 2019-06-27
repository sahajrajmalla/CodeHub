from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello World!, I'm in the project bro !!")


def vip(request):
    return HttpResponse("vip class goes here !")

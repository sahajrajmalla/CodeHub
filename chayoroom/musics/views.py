from django.shortcuts import render
from django.http import HttpResponse
from .models import new_add


def index(request):
    music_list = new_add.objects.all()
    return render(request, 'index2.html',
                  {'musics': music_list})

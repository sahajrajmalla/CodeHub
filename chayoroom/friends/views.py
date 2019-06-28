from django.shortcuts import render
from .models import friends
from django.http import HttpResponse

# Create your views here.


def friend(request):
    friend = friends.objects.all()
    return render(request, 'sahaj.html', {'friends': friend})

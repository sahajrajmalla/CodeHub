from django.shortcuts import render
from .models import friends

# Create your views here.


def friends(request):
    friend = friends.objects.all()
    return render(request, 'sahaj.html', {'friends': friend})

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def count(request):
    fulltext = request.GET['fulltext']
    words= fulltext.split()
    return render(request, 'count.html', {'fulltext': fulltext, 'count':len(words)})

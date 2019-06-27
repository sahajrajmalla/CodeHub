from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import customer
# Create your views here.


def index(request):

    userlist = customer.objects.all()
    return render(request, 'index.html', {'persons': userlist})


def vip(request):
    return HttpResponse("vip class goes here !")


def detail(request, customer_id):
    customer_detail = get_object_or_404(customer, id=customer_id)
    return render(request, 'detail.html', {'customer_detail': customer_detail})

from django.shortcuts import render

# Create your views here.


def friend(request):
    friends = friends.objects.all()
    return render(request, 'sahaj.html', {'friends': friends})

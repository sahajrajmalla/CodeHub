from django.shortcuts import render

# Create your views here.


def friends(request):
    friends = friends.objects.all()
    return render(request, 'sahaj.html', {'friends': friends})

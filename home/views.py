from django.shortcuts import render
from users.models import MyUser

def home(request):
    user = request.user

    name = user.name if request.user.is_authenticated else ""

    context = {
        'name': name,
    }
    
    return render(request, 'home.html', context)

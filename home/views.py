from django.shortcuts import render
from django.contrib.auth import get_user_model

def home(request):
    User = get_user_model()
    username = None
    if request.user.is_authenticated:
        username = request.user.get_full_name() or request.user.username
    
    return render(request, 'home.html', {'username': username})

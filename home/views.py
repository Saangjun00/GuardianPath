from django.shortcuts import render
from django.conf import settings

def home(request):
    context = {
        'KAKAO_CLIENT_ID': settings.SOCIALACCOUNT_PROVIDERS['kakao']['APP']['client_id'],
    }
    return render(request, 'home.html', context)

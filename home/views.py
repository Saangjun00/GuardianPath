from django.shortcuts import render
from map.models import UserRoute

def home(request):
    # 로그인된 사용자의 검색 기록을 불러옴
    if request.user.is_authenticated:
        search_history = UserRoute.objects.filter(user=request.user).order_by('-created_at')[:10]  # 최근 10개의 검색 기록
        favorite_routes = UserRoute.objects.filter(user=request.user, is_favorite=True)
    else:
        search_history = []
        favorite_routes = []

    return render(request, 'home.html', {
        'search_history': search_history,
        'favorite_routes': favorite_routes,
    })
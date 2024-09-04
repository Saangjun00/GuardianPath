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

    # 세션에서 출발지와 목적지 값을 가져옴
    departure = request.session.get('departure', '')
    destination = request.session.get('destination', '')
    
    # 세션에서 데이터 삭제 (다시 사용되지 않도록)
    request.session.pop('departure', None)
    request.session.pop('destination', None)

    return render(request, 'home.html', {
        'search_history': search_history,
        'favorite_routes': favorite_routes,
        'departure': departure,
        'destination': destination,
    })
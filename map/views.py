from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import UserRoute, SearchHistory
from users.models import User
from django.urls import reverse
from django.contrib import messages
import requests
from django.http import JsonResponse

def save_route(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        departure = request.POST.get('departure')
        destination = request.POST.get('destination')

        # 유저 타입이 입력되지 않은 경우
        if not user_type:
            messages.error(request, '유저 타입을 선택해주세요.')
            request.session['departure'] = departure
            request.session['destination'] = destination
            return redirect(reverse('home:home'))

        # 경로를 즐겨찾기로 저장
        if 'save_favorite' in request.POST:
            if request.user.is_authenticated:
                UserRoute.objects.create(
                    user = request.user,
                    user_type = user_type,
                    departure = departure,
                    destination = destination,
                    is_favorite = True
                )

            return redirect('home')

        # 경로 검색 로직 실행
        elif 'search_route' in request.POST:
            if request.user.is_authenticated:
                SearchHistory.objects.create(
                    user=request.user,
                    user_type=user_type,
                    departure=departure,
                    destination=destination
                )

            return redirect(reverse('search_results') + f"?departure={departure}&destination={destination}&user_type={user_type}")

    return redirect('home')

def search_results(request):
    # Tmap API 키
    tmap_api_key = settings.TMAP_API_KEY

    # GET 요청으로 전달된 출발지, 도착지 및 유저 타입 정보 가져오기
    departure = request.GET.get('departure')
    destination = request.GET.get('destination')
    user_type = request.GET.get('user_type')

    # GET 요청으로 전달된 경도 위도 가져오기
    departure_lat = request.GET.get('departure_lat')
    departure_lon = request.GET.get('departure_lon')
    destination_lat = request.GET.get('destination_lat')
    destination_lon = request.GET.get('destination_lon')

    # 길찾기 검색 결과 처리 (현재 미구현)
    results = 1

    context = {
        'tmap_api_key': tmap_api_key,
        'departure': departure,
        'destination': destination,
        'user_type': user_type,
        'results': results,
    }

    return render(request, 'search_results.html', context)

def clear_search_history(request):
    if request.user.is_authenticated:
        SearchHistory.objects.filter(user=request.user).delete()
        messages.success(request, '검색 기록이 삭제되었습니다.')
    
    return redirect(reverse('home:home'))

def delete_favorite_route(request, route_id):
    favorite_route = get_object_or_404(UserRoute, id=route_id, user=request.user, is_favorite=True)
    favorite_route.delete()

    return redirect('home')
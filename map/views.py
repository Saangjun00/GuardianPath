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
        departure_lat = request.POST.get('departure_lat')
        departure_lon = request.POST.get('departure_lon')
        destination_lat = request.POST.get('destination_lat')
        destination_lon = request.POST.get('destination_lon')

        # 세션 데이터 확인 로그 추가
        print('세션 데이터:', request.session.items())

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

            # 세션에 경로 관련 데이터를 저장
            request.session['user_type'] = user_type
            request.session['departure'] = departure
            request.session['destination'] = destination
            request.session['departure_lat'] = departure_lat
            request.session['departure_lon'] = departure_lon
            request.session['destination_lat'] = destination_lat
            request.session['destination_lon'] = destination_lon

            # 로그로 세션에 저장된 값 확인
            print(f'Session: {request.session.get("departure_lat")}, {request.session.get("departure_lon")}')
            print(f'Session: {request.session.get("destination_lat")}, {request.session.get("destination_lon")}')

            return redirect('search_results')

    return redirect('home')

def search_results(request):
    # Tmap API 키
    tmap_api_key = settings.TMAP_API_KEY

    # GET 요청으로 전달된 출발지, 도착지 및 유저 타입 정보 가져오기
    departure = request.session.get('departure')
    destination = request.session.get('destination')
    user_type = request.session.get('user_type')
    departure_lat = request.session.get('departure_lat')
    departure_lon = request.session.get('departure_lon')
    destination_lat = request.session.get('destination_lat')
    destination_lon = request.session.get('destination_lon')

    # 길찾기 검색 결과 처리 (현재 미구현)
    results = 1

    context = {
        'tmap_api_key': tmap_api_key,
        'departure': departure,
        'destination': destination,
        'user_type': user_type,
        'departure_lat': departure_lat,
        'departure_lon': departure_lon,
        'destination_lat': destination_lat,
        'destination_lon': destination_lon,
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
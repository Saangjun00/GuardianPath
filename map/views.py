from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import UserRoute, SearchHistory, ElevatorLocation, EscalatorLocation
from users.models import User
from django.urls import reverse
from django.contrib import messages
import json  # JSON 변환을 위해 import 추가

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
                    user=request.user,
                    user_type=user_type,
                    departure=departure,
                    destination=destination,
                    is_favorite=True
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

    return render(request, 'home.html')


def search_results(request):
    # Tmap API 키
    tmap_api_key = settings.TMAP_API_KEY

    # GET 요청으로 전달된 출발지, 도착지 및 유저 타입 정보 가져오기
    departure = request.GET.get('departure')
    destination = request.GET.get('destination')
    user_type = request.GET.get('user_type')

    # 길찾기 검색 결과 처리 (현재 미구현)
    results = 1  # 결과가 현재 미구현인 경우 임시 값으로 설정

    # 데이터베이스에서 엘리베이터 및 에스컬레이터 좌표 데이터 가져오기
    elevator_locations = ElevatorLocation.objects.all()
    escalator_locations = EscalatorLocation.objects.all()

    # 엘리베이터 위치 데이터를 JSON 형식으로 변환
    elevator_data = [
        {
            'lat': location.latitude,
            'lon': location.longitude
        }
        for location in elevator_locations
    ]

    # 에스컬레이터 위치 데이터를 JSON 형식으로 변환
    escalator_data = [
        {
            'lat': location.esc_latitude,
            'lon': location.esc_longitude
        }
        for location in escalator_locations
    ]

    # JSON 형식으로 변환
    elevator_data_json = json.dumps(elevator_data)
    escalator_data_json = json.dumps(escalator_data)

    # 템플릿에 전달할 컨텍스트 데이터 구성
    context = {
        'tmap_api_key': tmap_api_key,
        'departure': departure,
        'destination': destination,
        'user_type': user_type,
        'results': results,
        'elevator_data_json': elevator_data_json,  # 엘리베이터 위치 데이터
        'escalator_data_json': escalator_data_json,  # 에스컬레이터 위치 데이터
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




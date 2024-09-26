from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import UserRoute, SearchHistory
from users.models import User
from django.urls import reverse
from django.contrib import messages
from urllib.parse import urlencode
import requests
import json

def save_route(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        departure = request.POST.get('departure')
        destination = request.POST.get('destination')

        # 출발지와 도착지 입력 확인
        if not departure or not destination:
            messages.error(request, '출발지와 도착지를 모두 입력해주세요.')
            request.session['departure'] = departure
            request.session['destination'] = destination
            request.session['user_type'] = user_type
            return redirect(reverse('home:home'))

        # 유저 타입이 입력되지 않은 경우
        if not user_type:
            messages.error(request, '유저 타입을 선택해주세요.')
            request.session['departure'] = departure
            request.session['destination'] = destination
            request.session['user_type'] = user_type
            return redirect(reverse('home:home'))
        
        # 유효한 출발지 확인
        is_valid_departure, departure_msg = validate_address(departure)
        if not is_valid_departure:
            messages.error(request, departure_msg)  # 오류 메시지 사용
            request.session['departure'] = departure
            request.session['destination'] = destination
            return redirect(reverse('home:home'))

        # 유효한 도착지 확인
        is_valid_destination, destination_msg = validate_address(destination)
        if not is_valid_destination:
            messages.error(request, destination_msg)  # 오류 메시지 사용
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

            # 쿼리 파라미터를 생성하여 리디렉션
            query_params = {
                'user_type': user_type,
                'departure': departure,
                'destination': destination,
            }
            url = reverse('search_results') + '?' + urlencode(query_params)
            return redirect(url)

    return redirect('home')

def search_results(request):
    # Tmap API 키
    tmap_api_key = settings.TMAP_API_KEY

    # GET 요청으로 전달된 출발지, 도착지 및 유저 타입 정보 가져오기
    departure = request.GET.get('departure')
    destination = request.GET.get('destination')
    user_type = request.GET.get('user_type')

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

def validate_address(address):
    tmap_api_key = settings.TMAP_API_KEY
    url = f"https://apis.openapi.sk.com/tmap/geo/fullAddrGeo?version=1&format=json&callback=result&appKey={tmap_api_key}&coordType=WGS84GEO&fullAddr={address}"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # 'coordinateInfo'가 응답에 있는지 확인하고, 'newLon' 또는 'lon'이 있는지 확인
        if 'coordinateInfo' in data:
            coordinate = data['coordinateInfo'].get('coordinate', [])
            
            if len(coordinate) > 0:
                result = coordinate[0]  # 첫 번째 좌표를 가져옴
                
                # 'lat' 또는 'newLat'이 있는지 확인
                lat = result.get('lat') or result.get('newLat')
                lon = result.get('lon') or result.get('newLon')
                
                if lat and lon:
                    # 상세 주소 구성: 도로명과 건물번호, 건물명을 합쳐서 주소를 만듦
                    city_do = result.get('city_do', '')
                    gu_gun = result.get('gu_gun', '')
                    eup_myun = result.get('eup_myun', '')
                    legal_dong = result.get('legalDong', '')
                    ri = result.get('ri', '')
                    road_name = result.get('newRoadName', '')
                    building_index = result.get('newBuildingIndex', '')
                    building_name = result.get('newBuildingName', '')

                    bunji = result.get('bunji', '')

                    # 신주소 구성: 도로명, 건물번호, 건물명
                    full_address_new = f"{city_do} {gu_gun} {eup_myun} {road_name} {building_index} {building_name}".strip()
                    
                    # 구주소 구성: 법정동, 번지
                    full_address_old = f"{city_do} {gu_gun} {eup_myun} {legal_dong} {ri} {bunji}".strip()

                    # 최종 주소로 신주소 또는 구주소를 사용
                    full_address = full_address_new if road_name and building_index else full_address_old

                    # 상세 주소 체크: 번지수(건물번호)가 포함된 도로명 주소인지 확인
                    if not road_name or not building_index:
                        return False, "상세 주소까지 입력해주세요."
                    
                    # 상세 주소 체크: 번지수가 포함된 도로명 주소인지 확인
                    if len(full_address.split()) < 3:
                        return False, "상세 주소까지 입력해주세요."

                    # 상세 주소가 충분히 구체적인 경우
                    return True, None

    return False, "유효하지 않은 주소입니다."

def get_public_transport_route(departure, destination):
    tmap_api_key = settings.TMAP_API_KEY
    url = "https://apis.openapi.sk.com/tmap/routes/publicTransportation?version=1&format=json"

    headers = {
        'appKey': tmap_api_key
    }

    params = {
        'startX': departure['lon'] or departure['newLon'],  # 출발지 경도
        'startY': departure['lat'] or departure['newLat'],  # 출발지 위도
        'endX': destination['lon'] or destination['newLon'],  # 도착지 경도
        'endY': destination['lat'] or destination['newLat'],  # 도착지 위도
        'reqCoordType': 'WGS84GEO',
        'resCoordType': 'EPSG3857'
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
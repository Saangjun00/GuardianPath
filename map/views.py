from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserRoute
from users.models import User
from django.urls import reverse
from django.contrib import messages

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
                UserRoute.objects.create(
                    user=request.user,
                    user_type=user_type,
                    departure=departure,
                    destination=destination,
                    is_favorite=False
                )

            return redirect(reverse('search_results'))

    return render(request, 'home.html')

def search_results(request):
    # 길찾기 검색 로직에 따른 결과를 가져옴
    results = 1
    return render(request, 'search_results.html', {'results': results})

def clear_search_history(request):
    if request.user.is_authenticated:
        UserRoute.objects.filter(user=request.user, is_favorite=False).delete()
        messages.success(request, '검색 기록이 삭제되었습니다.')
    
    return redirect(reverse('home:home'))

def delete_favorite_route(request, route_id):
    favorite_route = get_object_or_404(UserRoute, id=route_id, user=request.user, is_favorite=True)
    favorite_route.delete()

    print(favorite_route)
    return redirect('home')

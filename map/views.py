from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserRoute
from users.models import User
from django.urls import reverse

def save_route(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        departure = request.POST.get('departure')
        destination = request.POST.get('destination')

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
            else:
                request.session['user_type'] = user_type
                request.session['departure'] = departure
                request.session['destination'] = destination
                request.session['is_favorite'] = True

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
            else:
                request.session['user_type'] = user_type
                request.session['departure'] = departure
                request.session['destination'] = destination

            return redirect(reverse('search_results'))

    return render(request, 'home.html')

def search_results(request):
    # 길찾기 검색 로직에 따른 결과를 가져옴
    results = 1
    return render(request, 'search_results.html', {'results': results})

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

User = get_user_model()

def register_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse("비밀번호가 일치하지 않습니다.")
        
        if User.objects.filter(email=email).exists():
            return HttpResponse("이메일이 이미 존재합니다.")
        
        # 사용자 생성
        User.objects.create_user(email=email, name=name, password=password1)
        return redirect('login_view')

    return render(request, 'login.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("잘못된 로그인입니다.")
    
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    auth_logout(request)
    return redirect('login_view')

@login_required
def profile_view(request):
    # 사용자 정보를 템플릿에 전달할 수 있습니다.
    return render(request, 'profile.html')

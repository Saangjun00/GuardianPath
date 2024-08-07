from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

User = get_user_model()

def register_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "비밀번호가 일치하지 않습니다.")
            return redirect('register_view')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "이메일이 이미 존재합니다.")
            return redirect('register_view')
        
        # 사용자 생성
        User.objects.create_user(email=email, name=name, password=password1)
        messages.success(request, "회원가입이 완료되었습니다. 로그인해주세요.")
        return redirect('login_view')

    return render(request, 'login.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "로그인 성공!")
            return redirect('home')
        else:
            messages.error(request, "로그인 실패했습니다.")
            return redirect('login_view')
        
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    auth_logout(request)
    messages.success(request, "로그아웃 되었습니다.")
    return redirect('home')

@login_required
def profile_view(request):
    # 사용자 정보를 템플릿에 전달할 수 있습니다.
    return render(request, 'profile.html')

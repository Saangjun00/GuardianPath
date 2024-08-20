from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from django.contrib import messages
from django.views import View
import re

def is_valid_password(password):
    # 비밀번호 길이 검사
    if len(password) < 8:
        return "비밀번호는 최소 8자 이상이어야 합니다."
    
    # 숫자 포함 여부 검사
    if not re.search(r"\d", password):
        return "비밀번호에는 숫자가 포함되어야 합니다."
    
    # 영문자 포함 여부 검사
    if not re.search(r"[A-Za-z]", password):
        return "비밀번호에는 영문자(대문자 또는 소문자)가 포함되어야 합니다."
    
    # 연속된 숫자 검사
    for i in range(len(password) - 2):
        if password[i:i+3].isdigit() and (int(password[i+1]) == int(password[i]) + 1 and int(password[i+2]) == int(password[i]) + 2):
            return "비밀번호에는 연속된 숫자가 포함될 수 없습니다."
    
    return None

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        # 비밀번호 일치 여부 확인
        if password1 != password2:
            messages.error(request, "비밀번호가 일치하지 않습니다.")
            return render(request, 'login.html', {
                'username': username,
                'email': email
            })
        
        # 비밀번호 유효성 검사
        password_error = is_valid_password(password1)
        if password_error:
            messages.error(request, password_error)
            return render(request, 'login.html', {
                'username': username,
                'email': email
            })
        
        # 사용자 이름 중복 확인
        if User.objects.filter(username=username).exists():
            messages.error(request, "해당 Username은 이미 사용 중입니다.")
            return render(request, 'login.html', {
                'username': username,
                'email': email
            })

        # 이메일 중복 확인
        if User.objects.filter(email=email).exists():
            messages.error(request, "해당 이메일 주소로 이미 계정이 존재합니다.")
            return render(request, 'login.html', {
                'username': username,
                'email': email
            })

        # 유저 생성
        user = User.objects.create_user(username, email, password1)
        user.save()
        messages.success(request, "회원가입이 완료되었습니다. 로그인해주세요!")
        return redirect('login_view')
    
    return render(request, 'login.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"{ username }님 환영합니다!")
            return redirect('home')
        else:
            messages.error(request, "로그인 실패했습니다.")
            return redirect('login_view')
        
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    messages.error(request, "로그아웃 되었습니다.")
    return redirect('home')

@login_required
def profile_view(request):
    # 사용자 정보를 템플릿에 전달할 수 있습니다.
    return render(request, 'profile.html')

class UserDeleteView(LoginRequiredMixin, View):
    def post(self, request, *arg, **kwargs):
        user = request.user
        if user.is_authenticated:
            logout(request)
            user.delete()

            messages.success(request, "계정이 삭제되었습니다.")
            return redirect('home')
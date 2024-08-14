from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, "비밀번호가 일치하지 않습니다.")
            return redirect('register_view')
        
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
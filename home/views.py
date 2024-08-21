from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('home')
    template_name = 'registration/password_change.html'  # 경로를 실제 템플릿 파일 경로로 수정

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'home.html'

    def dispatch(self, *args, **kwargs):
        # 메시지를 추가
        messages.success(self.request, "비밀번호가 성공적으로 변경되었습니다.")
        return super().dispatch(*args, **kwargs)
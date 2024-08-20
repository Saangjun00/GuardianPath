from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class MySocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):
        # 소셜 로그인 시도 시, 이메일을 확인
        email = sociallogin.user.email
        if email:
            try:
                # 이메일로 기존 유저를 검색
                existing_user = User.objects.get(email=email)
                
                if sociallogin.is_existing:
                    # 이미 연결된 소셜 계정이라면 통과
                    return

                # 이메일이 이미 존재한다면 로그인 페이지로 리다이렉트하고 메시지 표시
                messages.error(request, "이 이메일로 이미 계정이 존재합니다.<br>기존 계정으로 로그인해주세요.")
                raise ImmediateHttpResponse(redirect('login_view'))

            except User.DoesNotExist:
                pass  # 기존 계정이 없으면 새로 계정을 생성

    def save_user(self, request, sociallogin, form=None):
        # 기본 save_user 메소드 호출
        return super().save_user(request, sociallogin, form)
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialAccount
from django.core.exceptions import ValidationError
from .models import MyUser

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = sociallogin.user
        email = data.get('email')

        if email:
            try:
                # 사용자 모델에서 관리자(Manager)를 통해 쿼리
                existing_user = MyUser.objects.get(email=email)
                # 기존 사용자와 충돌하는 경우 처리
                user = existing_user
                sociallogin.user = user
            except MyUser.DoesNotExist:
                # 이메일이 없는 경우 새 사용자 생성
                user.email = email
        else:
            # Email 필드가 없는 경우, 예외를 발생시킬 수 있습니다.
            raise ValidationError("Email is required for social login.")
        user.save()
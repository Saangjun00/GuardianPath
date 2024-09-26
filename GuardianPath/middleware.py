import os
from django.http import HttpResponseForbidden
from django.conf import settings

class AdminIPWhitelistMiddleware:
    ALLOWED_IPS = [os.getenv('ALLOWED_IP_ADDRESS')]  # .env 파일에서 가져온 IP 주소

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and request.META['REMOTE_ADDR'] not in self.ALLOWED_IPS:
            return HttpResponseForbidden("You are not allowed to access this page.")
        return self.get_response(request)
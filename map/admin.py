from django.contrib import admin
from .models import UserRoute, SearchHistory, ElevatorLocation

@admin.register(UserRoute)
class UserRouteAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'departure', 'destination', 'is_favorite', 'created_at')
    search_fields = ('user__username', 'departure', 'destination')

# 중복 등록 제거
admin.site.register(SearchHistory)  # SearchHistory는 한 번만 등록
admin.site.register(ElevatorLocation)  # ElevatorLocation는 한 번만 등록

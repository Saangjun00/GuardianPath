from django.contrib import admin
from .models import UserRoute

@admin.register(UserRoute)
class UserRouteAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'departure', 'destination', 'is_favorite', 'created_at')
    search_fields = ('user__username', 'departure', 'destination')


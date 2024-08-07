from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission
from .models import MyUser

class UserAdmin(BaseUserAdmin):
    model = MyUser
    list_display = ('email', 'name', 'is_staff', 'is_active')  # 'first_name'과 'last_name' 대신 'name' 사용
    search_fields = ('email', 'name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')
    
    # Fieldsets: A list or tuple of tuples
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),  # 'first_name'과 'last_name' 대신 'name' 사용
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Add_fieldsets: A list or tuple of tuples
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )

admin.site.register(MyUser, UserAdmin)
admin.site.register(Permission)

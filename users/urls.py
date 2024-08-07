from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name="register_view"),
    path('login/', views.login_view, name='login_view'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name="home"),
]

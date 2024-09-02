from django.urls import path
from . import views

urlpatterns = [
    path('save_route/', views.save_route, name='save_route'),
    path('search_results/', views.search_results, name='search_results'),
]

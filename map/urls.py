from django.urls import path
from . import views

urlpatterns = [
    path('save_route/', views.save_route, name='save_route'),
    path('search_results/', views.search_results, name='search_results'),
    path('delete_favorite/<int:route_id>/', views.delete_favorite_route, name='delete_favorite_route'),
    path('clear_history/', views.clear_search_history, name='clear_search_history'),
]

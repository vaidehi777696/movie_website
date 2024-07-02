from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/', views.showtime_detail, name='showtime_detail'),
    # Add more URL patterns as needed
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Add URL patterns for seat selection, payment, confirmation, etc.
]
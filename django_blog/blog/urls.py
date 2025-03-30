from django.urls import path
from .views import home
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Django’s built-in login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Django’s built-in logout view
    path('profile/', views.profile, name='profile'),

]

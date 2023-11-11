from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('toot/', views.toot, name='toot'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('auth/', include('django.contrib.auth.urls')),
]


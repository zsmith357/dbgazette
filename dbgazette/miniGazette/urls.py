from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views 

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', views.home, name='home'),
    path('toot/', views.toot, name='toot'),
    path('register/', views.register, name='register'),
    path('auth/', include('django.contrib.auth.urls')),
]


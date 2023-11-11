from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('toot/', views.toot, name='toot'),
    path('register/', views.register, name='register'),
]


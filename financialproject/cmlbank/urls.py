from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('branches/', views.branches, name='branches'),
    path('registration/', views.registration, name='registration'),
    path('register/', views.register, name='register'),
    path('settings/', views.settings, name='settings'),
    path('get_branch/<int:district_id>/', views.get_branches, name='get_branch'),
]


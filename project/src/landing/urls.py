from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='landing-home'),
    path('picker/', views.picker, name='picker'),
    path('audience/', views.audience, name='audience-home'),
    path('presentation/<str:fileId>/', views.presentation, name='presentation-page'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy-policy'),
    #Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/',views.signup, name='signup'),
]
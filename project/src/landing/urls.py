from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='landing-home'),
    path('picker/', views.picker, name='picker'),
]

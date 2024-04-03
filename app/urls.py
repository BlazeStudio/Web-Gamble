# example/urls.py
from django.urls import path

from app import views


urlpatterns = [
    path('', views.index),
    path('high_low', views.high_low),
    path('bet', views.bet)
]
# example/urls.py
from django.urls import path

from app import views


urlpatterns = [
    path('', views.index),
    path('games', views.games),
    path('games/high_low', views.high_low),
    path('bet', views.bet)
]
# example/urls.py
from django.urls import path

from app import views


urlpatterns = [
    path('', views.home),
    path('games', views.games),
    path('games/high_low', views.high_low),
    path('bet', views.bet),
    path('games/mines', views.mines),
    path('get_cell_content', views.get_cell_content,),
    path('reveal_all_cells', views.reveal_all_cells,),
    path('start_game', views.start_game)
    # path('end_mines', views.end_mines)
]
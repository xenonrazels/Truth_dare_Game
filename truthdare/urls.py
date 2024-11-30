from django.urls import path
from .views import index,addPlayer,game_board_detail,spin_wheel

urlpatterns=[
    path('',index,name='index_page'),
    path('add_players/',addPlayer,name='add_player'),
    path('game_board/<int:game_board_id>/',game_board_detail, name='game_board_detail'),
    path('spin_wheel/<int:game_board_id>/',spin_wheel, name='spin_wheel'),
]
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('players/', views.players_index, name='index'),
  path('players/<int:player_id>/', views.players_detail, name='detail'),
  path('players/create/', views.PlayerCreate.as_view(), name='players_create'),
  path('players/<int:pk>/update', views.PlayerUpdate.as_view(), name='players_update'),
  path('players/<int:pk>/delete', views.PlayerDelete.as_view(), name='players_delete'),
  path('players/<int:player_id>/add_past_game/', views.add_past_game, name='add_past_game'),
]
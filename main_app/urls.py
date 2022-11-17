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
  path('players/<int:player_id>/assoc_skill/<int:skill_id>/', views.assoc_skill, name='assoc_skill'),
  path('players/<int:player_id>/unassoc_skill/<int:skill_id>/', views.unassoc_skill, name='unassoc_skill'),
  path('skills/', views.SkillList.as_view(), name='skills_index'),
  path('skills/<int:pk>/', views.SkillDetail.as_view(), name='skills_detail'),
  path('skills/create/', views.SkillCreate.as_view(), name='skills_create'),
  path('skills/<int:pk>/update/', views.SkillUpdate.as_view(), name='skills_update'),
  path('skills/<int:pk>/delete/', views.SkillDelete.as_view(), name='skills_delete'),
]
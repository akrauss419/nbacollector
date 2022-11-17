from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Player, Skill
from .forms import PastGameForm


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def players_index(request):
  players = Player.objects.all()
  return render(request, 'players/index.html', {
    'players': players
  })

def players_detail(request, player_id):
  player = Player.objects.get(id=player_id)
  id_list = player.skills.all().values_list('id')
  skills_player_doesnt_have = Skill.objects.exclude(id__in=id_list)
  past_game_form = PastGameForm()
  return render(request, 'players/detail.html', {
    'player': player, 
    'past_game_form': past_game_form,
    'skills': skills_player_doesnt_have
  })

class PlayerCreate(CreateView):
  model = Player
  fields = ['name', 'team', 'age', 'seasons', 'career_average_ppg']

class PlayerUpdate(UpdateView):
  model = Player
  fields = ['team', 'age', 'seasons', 'career_average_ppg']

class PlayerDelete(DeleteView):
  model = Player
  success_url = '/players'

def add_past_game(request, player_id):
  form = PastGameForm(request.POST)
  if form.is_valid():
    new_past_game = form.save(commit=False)
    new_past_game.player_id = player_id
    new_past_game.save()
  return redirect('detail', player_id=player_id)

class SkillList(ListView):
  model = Skill

class SkillDetail(DetailView):
  model = Skill

class SkillCreate(CreateView):
  model = Skill
  fields = '__all__'

class SkillUpdate(UpdateView):
  model = Skill
  fields = ['name', 'type']

class SkillDelete(DeleteView):
  model = Skill
  success_url = '/skills'

def assoc_skill(request, player_id, skill_id):
  Player.objects.get(id=player_id).skills.add(skill_id)
  return redirect('detail', player_id=player_id)

def unassoc_skill(request, player_id, skill_id):
  Player.objects.get(id=player_id).skills.remove(skill_id)
  return redirect('detail', player_id=player_id)
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player
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
  past_game_form = PastGameForm()
  return render(request, 'players/detail.html', {
    'player': player, 
    'past_game_form': past_game_form
  })

class PlayerCreate(CreateView):
  model = Player
  fields = '__all__'

class PlayerUpdate(UpdateView):
  model = Player
  fields = ['team', 'age', 'seasons', 'career_average_ppg']

class PlayerDelete(DeleteView):
  model = Player
  success_url = '/players'

def add_past_game(request, player_id):
  form = PastGameForm(request.POST)
  print(form)
  if form.is_valid():
    new_past_game = form.save(commit=False)
    new_past_game.player_id = player_id
    new_past_game.save()
  return redirect('detail', player_id=player_id)
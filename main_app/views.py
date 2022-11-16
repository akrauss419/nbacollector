from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Player


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
    return render(request, 'players/detail.html', {
        'player': player
    })

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'
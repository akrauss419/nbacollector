from django.shortcuts import render

players = [
    {'name': 'LeBron James', 'team': 'Los Angeles Lakers', 'age': 37, 'seasons': 20, 'career_average_points': 27.1},
    {'name': 'Jimmy Butler', 'team': 'Miami Heat', 'age': 33, 'seasons': 13, 'career_average_points': 17.8},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def players_index(request):
    return render(request, 'players/index.html', {
        'players': players
    })
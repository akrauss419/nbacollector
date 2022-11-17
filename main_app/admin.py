from django.contrib import admin
from .models import Player, PastGame, Skill


admin.site.register(Player)
admin.site.register(PastGame)
admin.site.register(Skill)
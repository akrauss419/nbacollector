from django.forms import ModelForm
from .models import PastGame

class PastGameForm(ModelForm):
  class Meta:
    model = PastGame
    fields = ['date', 'opponent', 'points_scored']
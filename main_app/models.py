from django.db import models
from django.urls import reverse
from datetime import date

OPPONENTS = (
  ('ATL', 'Atlanta Hawks'),
  ('BOS', 'Boston Celtics'),
  ('BKN', 'Brooklyn Nets'),
  ('CHA', 'Charlotte Hornets'),
  ('CHI', 'Chicago Bulls'),
  ('CLE', 'Cleveland Cavaliers'),
  ('DAL', 'Dallas Mavericks'),
  ('DEN', 'Denver Nuggets'),
  ('DET', 'Detroit Pistons'),
  ('GSW', 'Golden State Warriors'),
  ('HOU', 'Houston Rockets'),
  ('IND', 'Indiana Pacers'),
  ('LAC', 'Los Angeles Clippers'),
  ('LAL', 'Los Angeles Lakers'),
  ('MEM', 'Memphis Grizzlies'),
  ('MIA', 'Miami Heat'),
  ('MIL', 'Milwaukee Bucks'),
  ('MIN', 'Minnesota Timberwolves'),
  ('NOP', 'New Orleans Pelicans'),
  ('NYK', 'New York Knicks'),
  ('OKC', 'Oklahoma City Thunder'),
  ('ORL', 'Orlando Magic'),
  ('PHI', 'Philadelphia 76ers'),
  ('PHX', 'Phoenix Suns'),
  ('POR', 'Portland Trailblazers'),
  ('SAC', 'Sacramento Kings'),
  ('SAS', 'San Antonio Spurs'),
  ('TOR', 'Toronto Raptors'),
  ('UTA', 'Utah Jazz'),
  ('WAS', 'Washington Wizards')
)

TYPE = (
  ('O', 'Offense'),
  ('D', 'Defense'),
)

# Create your models here.
class Skill(models.Model):
  name = models.CharField(max_length=50)
  type = models.CharField(
    max_length=7,
    choices=TYPE,
    default=TYPE[0][0]
    )

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('skills_detail', kwargs={'pk': self.id})


class Player(models.Model):
  name = models.CharField(max_length=100)
  team = models.CharField(max_length=100)
  age = models.IntegerField()
  seasons = models.IntegerField()
  career_average_ppg = models.DecimalField(decimal_places=1, max_digits=3)
  skills = models.ManyToManyField(Skill)

  def __str__(self):
    return f"{self.name} ({self.id})"

  def get_absolute_url(self):
    return reverse('detail', kwargs={'player_id': self.id})


class PastGame(models.Model):
  date = models.DateField('Game Date')
  opponent = models.CharField(
    max_length=3,
    choices=OPPONENTS,
    default=OPPONENTS[0][0]
  )
  points_scored = models.IntegerField('Points Scored')

  player = models.ForeignKey(
    Player,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"Played {self.get_opponent_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']
from django.db import models

# Create your models here.
class Player(models.Model):
  name = models.CharField(max_length=100)
  team = models.CharField(max_length=100)
  age = models.IntegerField()
  seasons = models.IntegerField()
  career_average_ppg = models.DecimalField(decimal_places=1, max_digits=3)

  def __str__(self):
    return f"{self.name} ({self.id})"
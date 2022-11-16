# Generated by Django 4.1.3 on 2022-11-16 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_player_career_average_ppg'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastGames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Game Date')),
                ('opponent', models.CharField(choices=[('ATL', 'Atlanta Hawks'), ('BOS', 'Boston Celtics'), ('BKN', 'Brooklyn Nets'), ('CHA', 'Charlotte Hornets'), ('CHI', 'Chicago Bulls'), ('CLE', 'Cleveland Cavaliers'), ('DAL', 'Dallas Mavericks'), ('DEN', 'Denver Nuggets'), ('DET', 'Detroit Pistons'), ('GSW', 'Golden State Warriors'), ('HOU', 'Houston Rockets'), ('IND', 'Indiana Pacers'), ('LAC', 'Los Angeles Clippers'), ('LAL', 'Los Angeles Lakers'), ('MEM', 'Memphis Grizzlies'), ('MIA', 'Miami Heat'), ('MIL', 'Milwaukee Bucks'), ('MIN', 'Minnesota Timberwolves'), ('NOP', 'New Orleans Pelicans'), ('NYK', 'New York Knicks'), ('OKC', 'Oklahoma City Thunder'), ('ORL', 'Orlando Magic'), ('PHI', 'Philadelphia 76ers'), ('PHX', 'Phoenix Suns'), ('POR', 'Portland Trailblazers'), ('SAC', 'Sacramento Kings'), ('SAS', 'San Antonio Spurs'), ('TOR', 'Toronto Raptors'), ('UTA', 'Utah Jazz'), ('WAS', 'Washington Wizards')], default='ATL', max_length=3)),
                ('points_scored', models.IntegerField(verbose_name='Points Scored')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.player')),
            ],
        ),
    ]
from django.db import models


##### League models

class League(models.Model):
    logo_url = models.CharField(max_length=300)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Team(models.Model):
    league = models.ForeignKey(League)
    location = models.CharField(max_length=100)
    logo_url = models.CharField(max_length=300)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.location + " " + self.name


##### Playoff Season models

class PlayoffSeason(models.Model):
    league = models.ForeignKey(League)
    name = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team,blank=True)

    def __str__(self):
        return name


class PlayoffRound(models.Model):
    playoff_season = models.ForeignKey(PlayoffSeason)
    round_name = models.CharField(max_length=100)
    round_number = models.IntegerField()

    def __str__(self):
        return round_name or 'Round: ' + round_number


class SeriesActual(models.Model):
    playoff_round = models.ForeignKey(PlayoffRound)
    child_series = models.ForeignKey('self',blank=True)
    team1 = models.ForeignKey(Team,blank=True,related_name='+')
    team1_wins = models.IntegerField()
    team2 = models.ForeignKey(Team,blank=True,related_name='+')
    team2_wins = models.IntegerField()

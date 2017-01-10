from django.db import models


class League(models.Model):
    logo_url = models.CharField(max_length=300)
    name = models.CharField(max_length=100)


class Team(models.Model):
    league = models.ForeignKey(League)
    location = models.CharField(max_length=100)
    logo_url = models.CharField(max_length=300)
    name = models.CharField(max_length=100)

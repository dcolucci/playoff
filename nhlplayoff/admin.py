from django.contrib import admin
from .models import (
    League,
    PlayoffRound,
    PlayoffSeason,
    SeriesActual,
    Team
)

admin.site.register(League)
admin.site.register(PlayoffRound)
admin.site.register(PlayoffSeason)
admin.site.register(SeriesActual)
admin.site.register(Team)

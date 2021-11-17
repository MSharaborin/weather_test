from django.contrib import admin

from .models import Weather, Wind, Coord, Main


admin.site.register(Weather)
admin.site.register(Wind)
admin.site.register(Coord)
admin.site.register(Main)


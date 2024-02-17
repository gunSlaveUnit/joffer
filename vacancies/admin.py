from django.contrib import admin

from .models import Vacancy, Favorite, Hiding

admin.site.register(Hiding)
admin.site.register(Vacancy)
admin.site.register(Favorite)

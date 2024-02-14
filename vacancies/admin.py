from django.contrib import admin

from .models import Skill, Vacancy, Hiding

admin.site.register(Skill)
admin.site.register(Hiding)
admin.site.register(Vacancy)

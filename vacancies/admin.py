from django.contrib import admin

from .models import Vacancy, Favorite, Hiding, WorkFormat, EmploymentType

admin.site.register(Hiding)
admin.site.register(Vacancy)
admin.site.register(Favorite)
admin.site.register(WorkFormat)
admin.site.register(EmploymentType)

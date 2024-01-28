from django.views import generic

from .models import Vacancy


class VacancyList(generic.ListView):
    model = Vacancy
    context_object_name = "vacancy_list"

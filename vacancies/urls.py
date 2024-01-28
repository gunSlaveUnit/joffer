from django.urls import path

from .views import VacancyList, VacancyDetail

urlpatterns = [
    path('', VacancyList.as_view(), name='vacancy_list'),
    path('<int:pk>/', VacancyDetail.as_view(), name='vacancy_detail'),
]

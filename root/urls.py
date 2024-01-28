"""URL configuration for root project."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vacancies/', include('vacancies.urls')),
]
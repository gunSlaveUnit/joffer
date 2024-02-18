"""URL configuration for root project."""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('resumes/', include('resumes.urls')),
    path('vacancies/', include('vacancies.urls')),
    path('', TemplateView.as_view(template_name='root/index.html'), name='index'),
]

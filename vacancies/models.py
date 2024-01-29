from django.db import models

from root.models import Entity


class Vacancy(Entity):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'vacancies'

    def __str__(self):
        return self.title

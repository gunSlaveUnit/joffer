from django.db import models

from root.models import Entity


class Vacancy(Entity):
    title = models.CharField(max_length=100)

    salary_to = models.IntegerField(null=True, blank=True)
    salary_from = models.IntegerField(null=True, blank=True)

    experience_matter = models.BooleanField(default=False)
    experience_to = models.IntegerField(null=True, blank=True)
    experience_from = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'vacancies'

    def __str__(self):
        return self.title

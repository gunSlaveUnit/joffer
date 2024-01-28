from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'vacancies'

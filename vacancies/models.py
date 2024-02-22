from django.db import models

from shared.models import Entity, Skill


class WorkFormat(Entity):
    """Place where the employee carries out activities."""

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Vacancy(Entity):
    title = models.CharField(max_length=100)

    skills = models.ManyToManyField(Skill)

    salary_to = models.IntegerField(null=True, blank=True)
    salary_from = models.IntegerField(null=True, blank=True)

    experience_matter = models.BooleanField(default=False)
    experience_to = models.IntegerField(null=True, blank=True)
    experience_from = models.IntegerField(null=True, blank=True)

    work_format = models.ForeignKey(WorkFormat, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'vacancies'

    def __str__(self):
        return self.title


class Favorite(Entity):
    """The user can add a vacancy to the favorites."""

    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Hiding(Entity):
    """The user can hide a vacancy from the search results."""

    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

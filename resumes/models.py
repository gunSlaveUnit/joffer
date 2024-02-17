from django.db import models

from shared.models import Entity, Skill


class Resume(Entity):
    position = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.position


class SkillLevel(Entity):
    LEVELS = (
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert'),
        (5, 'Master'),
    )

    level = models.IntegerField(choices=LEVELS)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

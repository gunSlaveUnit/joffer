from django.db import models


class Entity(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Skill(Entity):
    """
    Represents ability or experience
    that the candidate should have (or already has)
    or be able to work with or have a personality trait.
    """

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

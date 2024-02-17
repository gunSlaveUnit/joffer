from django.db import models

from root.models import Entity


class Resume(Entity):
    position = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

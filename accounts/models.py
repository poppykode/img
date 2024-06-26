import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from core.enums import RoleEnum

# Create your models here.
class User (AbstractUser):
    class Role(models.TextChoices):
        CANDIDATE = RoleEnum.CANDIDATE.value
        COACH = RoleEnum.COACH.value
        ADMIN = RoleEnum.ADMIN.value

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length = 100,choices = Role.choices, default = Role.ADMIN)

    def __str__(self):
        return self.first_name.capitalize() + ' ' + self.last_name.capitalize() + ' | ' + str(self.email)

    class Meta:
        ordering = ["-date_joined", ]

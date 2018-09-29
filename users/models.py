from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=45, blank=True)
    favorite_treat = models.CharField(max_length=20, blank=True)
    def __repr__(self):
        return f"User object: {self.username}"
    def display_name(self):
        last_name = self.last_name[0] + "." if len(self.last_name) > 0 else ''
        return f"{self.first_name} {last_name}"
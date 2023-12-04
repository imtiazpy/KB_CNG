from django.db import models
from django.contrib.auth.models import AbstractUser 



class User(AbstractUser):
  name = models.CharField(max_length=100, null=True)
  designation = models.CharField(max_length=100, blank=True, null=True)

  def save(self, *args, **kwargs):
    # Hash the password before saving
    self.set_password(self.password)
    super().save(*args, **kwargs)

  def __str__(self):
    return f"{self.name}"


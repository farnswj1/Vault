from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class User(AbstractUser):
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def get_absolute_url(self):
        return reverse("users:detail", args=(self.pk,))
    
    class Meta:
        ordering = ("username",)
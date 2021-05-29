from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    ProhibitNullCharactersValidator
)
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Key(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    key = models.CharField(
        max_length=30,
        null=False,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(30),
            ProhibitNullCharactersValidator()
        ]
    )
    value = models.TextField(
        max_length=5000,
        null=False,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(5000),
            ProhibitNullCharactersValidator()
        ]
    )
    notes = models.TextField(max_length=1000, null=True)

    def get_absolute_url(self):
        return reverse("keys:detail", args=(self.pk,))
    
    def __str__(self):
        return "Key: " + self.key

    class Meta:
        ordering = ("key",)
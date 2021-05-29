from django.forms import ModelForm
from .models import Key

class KeyForm(ModelForm):
    class Meta:
        model = Key
        exclude = ("user",)
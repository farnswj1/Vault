from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")


class StaffUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "is_staff", "is_superuser")
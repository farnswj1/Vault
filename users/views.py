from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from .models import User
from .forms import UserCreateForm, UserUpdateForm, StaffUpdateForm
from .mixins import UserIsStaffOrAdminMixin
from .filters import UserFilterSet

# Create your views here.
class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = "users/create.html"
    model = User
    form_class = UserCreateForm
    success_message = "User account was created successfully!"
    extra_context = {"title": "Register"}

    def get_success_url(self):
        return reverse("base:home")


class UserListView(UserIsStaffOrAdminMixin, FilterView):
    template_name = "users/list.html"
    filterset_class = UserFilterSet
    context_object_name = "users"
    paginate_by = 15
    extra_context = {"title": "List of Users"}

    def get_queryset(self):
        return User.objects.filter(is_active=True)


class UserDetailView(UserIsStaffOrAdminMixin, DetailView):
    template_name = "users/detail.html"
    model = User
    context_object_name = "user_"
    extra_context = {"title": "User Information"}


class UserUpdateView(UserIsStaffOrAdminMixin, SuccessMessageMixin, UpdateView):
    template_name = "users/update.html"
    model = User
    form_class = UserUpdateForm
    context_object_name = "user_"
    success_message = "User account was updated successfully!"
    extra_context = {"title": "Update User"}


class UserDeleteView(UserIsStaffOrAdminMixin, DeleteView):
    template_name = "users/delete.html"
    model = User
    context_object_name = "user_"
    success_message = "User account was deleted successfully!"
    extra_context = {"title": "Delete User"}

    def delete(self, request, *args, **kwargs):
        user_ = self.get_object()
        user_.is_active = False
        user_.save()
        messages.success(self.request, self.success_message)
        return redirect("users:list")


class UserLoginView(LoginView):
    template_name = "users/login.html"
    extra_context = {"title": "Login"}


class UserLogoutView(LogoutView):
    pass
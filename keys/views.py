from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Key
from .forms import KeyForm
from .mixins import UserOwnsKeyMixin
from .filters import KeyFilterSet

# Create your views here.
class KeyCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "keys/create.html"
    model = Key
    form_class = KeyForm
    success_message = "Key was created successfully!"
    extra_context = {"title": "New Key"}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class KeyListView(LoginRequiredMixin, FilterView):
    template_name = "keys/list.html"
    filterset_class = KeyFilterSet
    context_object_name = "keys"
    paginate_by = 15
    extra_context = {"title": "My Keys"}

    def get_queryset(self):
        return Key.objects.filter(user=self.request.user)


class KeyDetailView(UserOwnsKeyMixin, DetailView):
    template_name = "keys/detail.html"
    model = Key
    context_object_name = "key"
    extra_context = {"title": "Key Information"}


class KeyUpdateView(UserOwnsKeyMixin, SuccessMessageMixin, UpdateView):
    template_name = "keys/update.html"
    model = Key
    form_class = KeyForm
    success_message = "Key was created successfully!"
    extra_context = {"title": "Update Key"}


class KeyDeleteView(UserOwnsKeyMixin, DeleteView):
    template_name = "keys/delete.html"
    model = Key
    success_url = reverse_lazy("keys:list")
    success_message = "Key was deleted successfully!"
    extra_context = {"title": "Delete Key"}

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return super().get_success_url()
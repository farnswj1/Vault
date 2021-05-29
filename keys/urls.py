from django.urls import path
from . import views

app_name = "keys"

urlpatterns = [
    path("", views.KeyListView.as_view(), name="list"),
    path("create/", views.KeyCreateView.as_view(), name="create"),
    path("<int:pk>/", views.KeyDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", views.KeyUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.KeyDeleteView.as_view(), name="delete"),
]
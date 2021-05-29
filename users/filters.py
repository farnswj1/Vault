from django_filters import FilterSet, CharFilter, BooleanFilter
from .models import User

class UserFilterSet(FilterSet):
    username = CharFilter("username", label="Username", lookup_expr="icontains")
    is_staff = BooleanFilter("is_staff", label="Staff")
    is_superuser = BooleanFilter("is_superuser", label="Administrator")

    class Meta:
        model = User
        fields = ("username", "is_staff", "is_superuser")
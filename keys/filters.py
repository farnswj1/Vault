from django_filters import FilterSet, CharFilter
from .models import Key

class KeyFilterSet(FilterSet):
    key = CharFilter("key", label="Key", lookup_expr="icontains")

    class Meta:
        model = Key
        fields = ("key",)
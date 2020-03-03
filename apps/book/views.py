from rest_framework import viewsets
from django_filters import rest_framework as filters
from .serializers import BookSerializer
from .models import Book


class BookFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains"
    )

    publication_year = filters.CharFilter(
        field_name="publication_year",
        lookup_expr="exact"
    )

    edition = filters.CharFilter(
        field_name="edition",
        lookup_expr="exact"
    )

    author = filters.CharFilter(
        field_name="authors__name",
        lookup_expr="icontains"
    )

    class Meta:
        model = Book
        fields = ["name", "publication_year", "edition", "author"]


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter

    def get_queryset(self):
        queryset = Book.objects.all().order_by(
            'name'
        )
        return queryset

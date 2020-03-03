from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .serializers import AuthorSerializer
from .models import Author


class AuthorFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Author
        fields = ["name"]


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    http_method_names = ['get']
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AuthorFilter

    def get_queryset(self):
        queryset = Author.objects.all().order_by(
            'name'
        )
        return queryset

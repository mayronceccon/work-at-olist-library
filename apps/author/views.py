from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AuthorSerializer
from .models import Author


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Author.objects.all().order_by(
            '-name'
        )

        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(
                name__icontains=name
            )
        return queryset

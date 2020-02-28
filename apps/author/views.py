from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AuthorSerializer
from .models import Author


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    http_method_names = ['get']

    def get_queryset(self):
        return Author.objects.all()

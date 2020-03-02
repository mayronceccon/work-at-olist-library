from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all().order_by(
            'name'
        )

        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(
                name__icontains=name
            )

        publication_year = self.request.query_params.get(
            'publication_year',
            None
        )
        if publication_year is not None:
            queryset = queryset.filter(
                publication_year=publication_year
            )

        edition = self.request.query_params.get('edition', None)
        if edition is not None:
            queryset = queryset.filter(
                edition=edition
            )

        author = self.request.query_params.get('author', None)
        if author is not None:
            if author.isnumeric():
                queryset = queryset.filter(
                    authors__id=author
                )
            else:
                queryset = queryset.filter(
                    authors__name__icontains=author
                )
        return queryset

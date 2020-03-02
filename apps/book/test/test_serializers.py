from django.test import TestCase
from apps.author.models import Author
from apps.book.models import Book
from apps.book.serializers import BookSerializer


class BookSerializerTest(TestCase):
    def setUp(self):
        self.__book = self.__book_python_and_django()
        self.__serializer = BookSerializer(instance=self.__book)

    def __create_author_osvaldo(self):
        author = Author(
            name="Osvaldo Santana Neto"
        )
        author.save()
        return author

    def __book_python_and_django(self):
        book = Book()
        book.name = "Python E Django - Desenvolvimento Agil De Aplicacoes Web"
        book.publication_year = 2010
        book.edition = "1"
        book.save()
        book.authors.add(self.__create_author_osvaldo())
        return book

    def test_book_serializer_keys(self):
        data = self.__serializer.data
        self.assertEqual(
            set(data.keys()),
            set([
                "id", "name", "edition",
                "publication_year", "authors"
            ])
        )

    def test_book_serializer_values(self):
        data = self.__serializer.data

        self.assertEqual(
            self.__book.name,
            data["name"]
        )
        self.assertEqual(
            self.__book.publication_year,
            data["publication_year"]
        )
        self.assertEqual(
            self.__book.edition,
            data["edition"]
        )
        self.assertEqual(
            list(self.__book.authors.values_list("id", flat=True)),
            data["authors"]
        )

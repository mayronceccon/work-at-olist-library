from django.test import TestCase
from django.db.utils import IntegrityError
from apps.author.models import Author
from apps.book.models import Book


class BookModelsTest(TestCase):
    def setUp(self):
        self.__create_author_osvaldo()
        self.__create_author_thiago()
        self.__create_author_luciano()

    def __create_author_osvaldo(self):
        author = Author(
            name="Osvaldo Santana Neto"
        )
        author.save()
        self.__author_osvaldo = author

    def __create_author_thiago(self):
        author = Author(
            name="Thiago Galesi"
        )
        author.save()
        self.__author_thiago = author

    def __create_author_luciano(self):
        author = Author(
            name="Luciano Ramalho"
        )
        author.save()
        self.__author_luciano = author

    def __book_python_and_django(self):
        book = Book()
        book.name = "Python E Django - Desenvolvimento Agil De Aplicacoes Web"
        book.publication_year = 2010
        book.edition = 1
        book.save()
        book.authors.add(self.__author_osvaldo)
        book.authors.add(self.__author_thiago)
        return book

    def __book_fluent_python(self):
        book = Book()
        book.name = "Fluent Python"
        book.publication_year = 2015
        book.edition = 1
        book.save()
        book.authors.add(self.__author_luciano)
        return book

    def test_insert_ok_book(self):
        book = self.__book_python_and_django()

        self.assertEqual(1, book.id)
        self.assertEqual(
            "Python E Django - Desenvolvimento Agil De Aplicacoes Web",
            book.name
        )
        self.assertEqual(2010, book.publication_year)

        find_authors = [author.name for author in book.authors.all()]
        self.assertCountEqual(
            find_authors,
            [
                "Thiago Galesi",
                "Osvaldo Santana Neto"
            ]
        )

    def test_update_ok_book(self):
        self.__book_python_and_django()

        book = Book.objects.get(pk=1)
        book.name = "New Name Book"
        book.publication_year = 2000
        book.save()

        self.assertEqual(1, book.id)
        self.assertEqual(
            "New Name Book",
            book.name
        )
        self.assertEqual(2000, book.publication_year)

        find_authors = [author.name for author in book.authors.all()]
        self.assertCountEqual(
            find_authors,
            [
                "Thiago Galesi",
                "Osvaldo Santana Neto"
            ]
        )

    def test_delete_ok_book(self):
        self.__book_python_and_django()

        book = Book.objects.get(pk=1)
        book.delete()

        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(pk=1)

    def test_get_book(self):
        book = self.__book_python_and_django()
        books = Book.objects.get(pk=book.id)

        self.assertEqual(1, book.id)
        self.assertEqual(
            "Python E Django - Desenvolvimento Agil De Aplicacoes Web",
            book.name
        )
        self.assertEqual(2010, book.publication_year)

        find_authors = [author.name for author in book.authors.all()]
        self.assertCountEqual(
            find_authors,
            [
                "Thiago Galesi",
                "Osvaldo Santana Neto"
            ]
        )

    def test_get_all_books(self):
        self.__book_python_and_django()
        self.__book_fluent_python()

        books = Book.objects.all()
        find_books = [book.name for book in books]
        self.assertCountEqual(
            find_books,
            [
                "Python E Django - Desenvolvimento Agil De Aplicacoes Web",
                "Fluent Python"
            ]
        )

    def test_unique_name_version(self):
        self.__book_python_and_django()
        with self.assertRaises(IntegrityError):
            self.__book_python_and_django()

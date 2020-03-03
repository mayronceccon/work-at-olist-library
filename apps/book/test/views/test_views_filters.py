from django.test import TestCase, Client
from apps.author.models import Author
from apps.book.models import Book

client = Client()


class BookViewFiltersTest(TestCase):
    def __create_author_osvaldo(self):
        author = Author(
            name="Osvaldo Santana Neto"
        )
        author.save()
        self.__author = author

    def __book_python_and_django(self):
        book = Book()
        book.name = "Python E Django - Desenvolvimento Agil De Aplicacoes Web"
        book.publication_year = 2010
        book.edition = "1"
        book.save()
        book.authors.add(self.__author)
        self.__book = book

    def __create_book_fluent_python(self):
        author = Author(
            name="Luciano Ramalho"
        )
        author.save()

        book = Book()
        book.name = "Fluent Python"
        book.publication_year = 2015
        book.edition = 2
        book.save()
        book.authors.add(author)

    def __start_data_filters(self):
        self.__create_author_osvaldo()
        self.__book_python_and_django()
        self.__create_book_fluent_python()

    def test_filter_name_author(self):
        self.__start_data_filters()

        filter_name = "Django"
        response = client.get(f"/api/v1/books/?name={filter_name}")

        find_books = [
            book['name']
            for book in response.json()['results']
        ]
        self.assertCountEqual(
            find_books,
            ["Python E Django - Desenvolvimento Agil De Aplicacoes Web"]
        )

    def test_filter_publication_year(self):
        self.__start_data_filters()

        year = 2015
        response = client.get(f"/api/v1/books/?publication_year={year}")

        find_books = [
            book['name']
            for book in response.json()['results']
        ]
        self.assertCountEqual(
            find_books,
            ["Fluent Python"]
        )

    def test_filter_edition(self):
        self.__start_data_filters()

        filter_edition = 2
        response = client.get(f"/api/v1/books/?edition={filter_edition}")

        find_books = [
            book['name']
            for book in response.json()['results']
        ]
        self.assertCountEqual(
            find_books,
            ["Fluent Python"]
        )

    def test_filter_author_id(self):
        self.__start_data_filters()

        filter_author = 1
        response = client.get(f"/api/v1/books/?author={filter_author}")

        find_books = [
            book['name']
            for book in response.json()['results']
        ]
        self.assertCountEqual(
            find_books,
            ["Python E Django - Desenvolvimento Agil De Aplicacoes Web"]
        )

    def test_filter_author_name(self):
        self.__start_data_filters()

        filter_author = "Osvaldo"
        response = client.get(f"/api/v1/books/?author={filter_author}")

        find_books = [
            book['name']
            for book in response.json()['results']
        ]
        self.assertCountEqual(
            find_books,
            ["Python E Django - Desenvolvimento Agil De Aplicacoes Web"]
        )

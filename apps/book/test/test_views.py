from django.test import TestCase, Client
from rest_framework import status
from apps.author.models import Author
from apps.book.models import Book
from apps.book.serializers import BookSerializer

client = Client()


class BookViewTest(TestCase):
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

    def __data_book(self):
        return {
            "name": "My first book",
            "edition": "1",
            "publication_year": 2017,
            "authors": [
                self.__author.id
            ]
        }

    def test_get_book(self):
        self.__create_author_osvaldo()
        self.__book_python_and_django()

        response = client.get(f"/api/v1/books/{self.__book.id}/")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.__book.id, response.data["id"])
        self.assertEqual(self.__book.name, response.data["name"])
        self.assertEqual(self.__book.edition, response.data["edition"])
        self.assertEqual(
            list(self.__book.authors.values_list("id", flat=True)),
            response.data["authors"]
        )

    def test_get_book_404(self):
        response = client.get("/api/v1/books/404/")
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_get_all_books(self):
        self.__create_author_osvaldo()
        self.__book_python_and_django()

        response = client.get("/api/v1/books/")

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertCountEqual(response.data['results'], serializer.data)

    def test_create_book_data(self):
        self.__create_author_osvaldo()
        data = self.__data_book()
        response = client.post("/api/v1/books/", data)
        new_id = response.data["id"]
        book = Book.objects.get(pk=new_id)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(data["name"], book.name)
        self.assertEqual(data["edition"], book.edition)
        self.assertEqual(
            response.data["authors"],
            list(book.authors.values_list("id", flat=True))
        )

    def test_update_book_data(self):
        self.__create_author_osvaldo()
        self.__book_python_and_django()
        data = self.__data_book()

        response = client.put(
            f"/api/v1/books/{self.__book.id}/",
            data,
            content_type="application/json"
        )

        book = Book.objects.get(pk=self.__book.id)
        self.assertEqual(data["name"], book.name)
        self.assertEqual(data["edition"], book.edition)
        self.assertEqual(
            response.data["authors"],
            list(book.authors.values_list("id", flat=True))
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_update_book_404(self):
        response = client.put(
            "/api/v1/books/404/",
            {},
            content_type="application/json"
        )
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_delete_book(self):
        self.__create_author_osvaldo()
        self.__book_python_and_django()

        response = client.delete(f"/api/v1/books/{self.__book.id}/")

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(pk=self.__book.id)

    def test_delete_book_404(self):
        response = client.delete("/api/v1/books/404/")
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

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

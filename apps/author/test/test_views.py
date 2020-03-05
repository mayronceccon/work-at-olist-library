from django.test import TestCase, Client
from rest_framework import status
from apps.author.models import Author
from apps.author.serializers import AuthorSerializer

client = Client()


class AuthorViewTest(TestCase):
    def setUp(self):
        self.__author_luciano = Author(
            name="Luciano Ramalho"
        )
        self.__author_luciano.save()

        self.__author_osvaldo = Author(
            name="Osvaldo Santana Neto"
        )
        self.__author_osvaldo.save()

    def test_get_author(self):
        author_id = self.__author_luciano.id
        response = client.get(f'/api/v1/authors/{author_id}/')
        author = Author.objects.get(pk=author_id)

        self.assertEqual(author.id, response.data['id'])
        self.assertEqual(author.name, response.data['name'])
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_all_authors(self):
        response = client.get('/api/v1/authors/')

        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)

        self.assertCountEqual(response.data['results'], serializer.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_author_404(self):
        response = client.get('/api/v1/authors/404/')
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_get_all_filter_name(self):
        name_filter = "Luciano"
        response = client.get(f'/api/v1/authors/?name={name_filter}')

        find_authors = [
            author['name']
            for author in response.json()['results']
        ]
        self.assertCountEqual(
            find_authors,
            ["Luciano Ramalho"]
        )

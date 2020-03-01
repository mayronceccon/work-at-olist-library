from django.test import TestCase
from django.db.utils import IntegrityError
from apps.author.models import Author


class AuthorModelsTest(TestCase):
    def __create_author_luciano(self):
        author = Author(
            name="Luciano Ramalho"
        )
        author.save()
        return author

    def __create_author_osvaldo(self):
        author = Author(
            name="Osvaldo Santana Neto"
        )
        author.save()
        return author

    def test_get_author(self):
        self.__create_author_luciano()
        author = Author.objects.get(pk=1)

        self.assertEqual(1, author.id)
        self.assertEqual("Luciano Ramalho", author.name)

    def test_get_all_authors(self):
        self.__create_author_luciano()
        self.__create_author_osvaldo()

        authors = Author.objects.all()

        find_authors = [author.name for author in authors]
        self.assertCountEqual(
            find_authors,
            ["Luciano Ramalho", "Osvaldo Santana Neto"]
        )

        self.assertEqual(2, Author.objects.count())

    def test_unique_author(self):
        self.__create_author_luciano()
        with self.assertRaises(IntegrityError):
            self.__create_author_luciano()

    def test_str_author(self):
        self.__create_author_luciano()
        author = Author.objects.get(pk=1)
        self.assertEqual("Luciano Ramalho", str(author))

    def test_strip_name_author(self):
        author_model = Author(
            name="   Osvaldo Santana Neto   "
        )
        author_model.save()

        author = Author.objects.get(pk=1)

        self.assertEqual(1, author.id)
        self.assertEqual("Osvaldo Santana Neto", author.name)

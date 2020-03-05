from django.test import TestCase
from django.db.utils import IntegrityError
from apps.author.models import Author


class AuthorModelsTest(TestCase):
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
        author = Author.objects.get(id=self.__author_luciano.id)

        self.assertEqual(self.__author_luciano.id, author.id)
        self.assertEqual("Luciano Ramalho", author.name)

    def test_get_all_authors(self):
        authors = Author.objects.all()

        find_authors = [author.name for author in authors]
        self.assertCountEqual(
            find_authors,
            ["Luciano Ramalho", "Osvaldo Santana Neto"]
        )

        self.assertEqual(2, Author.objects.count())

    def test_unique_author(self):
        with self.assertRaises(IntegrityError):
            author = Author(
                name="Luciano Ramalho"
            )
            author.save()

    def test_str_author(self):
        author = Author.objects.get(id=self.__author_luciano.id)
        self.assertEqual("Luciano Ramalho", str(author))

    def test_strip_name_author(self):
        author_model = Author(
            name="   Dan Brown   "
        )
        author_model.save()

        author = Author.objects.get(id=author_model.id)

        self.assertEqual(author_model.id, author.id)
        self.assertEqual("Dan Brown", author.name)

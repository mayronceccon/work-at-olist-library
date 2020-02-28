from django.test import TestCase
from django.db.utils import IntegrityError
from apps.author.models import Author


class AuthorModelsTest(TestCase):
    def setUp(self):
        author_model = Author(
            name="Luciano Ramalho"
        )
        author_model.save()

    def test_get_author(self):
        author = Author.objects.get(pk=1)

        self.assertEqual(1, author.id)
        self.assertEqual("Luciano Ramalho", author.name)

    def test_get_all_authors(self):
        author_model = Author(
            name="Osvaldo Santana Neto"
        )
        author_model.save()

        authors = Author.objects.all()

        find_authors = [author.name for author in authors]
        self.assertCountEqual(
            find_authors,
            ["Luciano Ramalho", "Osvaldo Santana Neto"]
        )

        self.assertEqual(2, Author.objects.count())

    def test_unique_author(self):
        with self.assertRaises(IntegrityError):
            author_model = Author(
                name="Luciano Ramalho"
            )
            author_model.save()

    def test_str_author(self):
        author = Author.objects.get(pk=1)
        self.assertEqual("Luciano Ramalho", str(author))

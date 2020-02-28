import os
from io import StringIO
from django.core.management import call_command
from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TransactionTestCase
from apps.author.models import Author

PATH_FILE = os.path.dirname(os.path.abspath(__file__))


class ImportAuthorsCommandsTest(TransactionTestCase):
    def test_command_output_all_created(self):
        out = StringIO()
        try:
            call_command(
                "import_authors",
                os.path.join(PATH_FILE, "authors.csv"),
                stdout=out
            )
            expected = """Luciano Ramalho created\nOsvaldo Santana Neto created\n"""
            self.assertEqual(expected, out.getvalue())

            authors = Author.objects.all()
            find_authors = [author.name for author in authors]
            self.assertCountEqual(
                find_authors,
                ["Luciano Ramalho", "Osvaldo Santana Neto"]
            )
            self.assertEqual(2, Author.objects.count())

        finally:
            out.close()

    def test_command_output_already_created(self):
        author_model = Author(
            name="Luciano Ramalho"
        )
        author_model.save()
        out = StringIO()

        try:
            call_command(
                "import_authors",
                os.path.join(PATH_FILE, "authors.csv"),
                stdout=out
            )

            expected = """Luciano Ramalho already created\nOsvaldo Santana Neto created\n"""
            self.assertEqual(expected, out.getvalue())

            authors = Author.objects.all()
            find_authors = [author.name for author in authors]
            self.assertCountEqual(
                find_authors,
                ["Luciano Ramalho", "Osvaldo Santana Neto"]
            )
            self.assertEqual(2, Author.objects.count())
        finally:
            out.close()

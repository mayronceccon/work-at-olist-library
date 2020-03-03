from django.test import TestCase
from utils.import_data import ImportData
from apps.book.models import Book


class ImportDataTest(TestCase):
    def test_import_message_first_name(self):
        data = [
            {"name": "Book 1", "edition": "1", "publication_year": "2019"},
            {"name": "Book 2", "edition": "2", "publication_year": "2020"},
        ]

        import_data = ImportData(Book, data)
        import_data.execute()

        messages = import_data.get_messages()
        find_authors = [message for message in messages]
        self.assertCountEqual(
            find_authors,
            ["Book 1 created", "Book 2 created"]
        )

    def test_import_message_first_edition(self):
        data = [
            {"edition": "v1", "publication_year": "2019", "name": "Book 1"},
            {"edition": "v2", "publication_year": "2020", "name": "Book 2"},
        ]

        import_data = ImportData(Book, data)
        import_data.execute()

        messages = import_data.get_messages()
        find_authors = [message for message in messages]
        self.assertCountEqual(
            find_authors,
            ["v1 created", "v2 created"]
        )

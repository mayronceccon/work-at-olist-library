import os
from django.test import TestCase
from utils.file_read import FileRead

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class FileReadTest(TestCase):
    def test_data(self):
        file_read_csv = os.path.join(BASE_DIR, "file_read.csv")
        file_read = FileRead(file_read_csv)
        file_read.execute()

        data = file_read.get_data()

        expected = [
            {"name": "Book 1", "edition": "1", "publication_year": "2019"},
            {"name": "Book 2", "edition": "2", "publication_year": "2020"},
        ]
        self.assertEqual(expected, data)

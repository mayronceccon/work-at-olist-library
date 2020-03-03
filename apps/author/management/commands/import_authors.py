from django.core.management.base import BaseCommand
from utils.file_read import FileRead
from .utils.import_data import ImportData
from apps.author.models import Author


class Command(BaseCommand):
    help = "Create Authors"

    def __init__(self, stdout=None, stderr=None):
        super().__init__(stdout=stdout, stderr=stderr)
        self.__data = []
        self.__messages = []

    def add_arguments(self, parser):
        parser.add_argument(
            "files",
            nargs='+',
            type=str,
            help="CSV file with the authors"
        )

    def handle(self, *args, **options):
        self.__files = options["files"]
        if not self.__files:
            return

        for file_import in self.__files:
            self.__file_read(file_import)
            self.__import_authors()
            self.__show_messages()

    def __file_read(self, file_import):
        file = FileRead(file_import)
        file.execute()
        self.__data = file.get_data()

    def __import_authors(self):
        import_authors = ImportData(Author, self.__data)
        import_authors.execute()
        self.__messages = import_authors.get_messages()

    def __show_messages(self):
        for message in self.__messages:
            self.stdout.write(message)

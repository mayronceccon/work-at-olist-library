import csv
import contextlib
from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand
from apps.author.models import Author


class Command(BaseCommand):
    help = "Create Authors"

    def __init__(self, stdout=None, stderr=None):
        super().__init__(stdout=stdout, stderr=stderr)
        self.__authors = []
        self.__files = []

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
        self.__list_files()
        self.__list_authors()

    def __list_files(self):
        for file_import in self.__files:
            self.__open_file(file_import)

    def __open_file(self, file_import):
        with open(file_import, newline="") as csvfile:
            self.__read_file(csvfile)

    def __read_file(self, csvfile):
        reader = csv.reader(csvfile, delimiter=";", quotechar='"')
        self.__list_register(reader)

    def __list_register(self, reader):
        for (key, row) in enumerate(reader):
            if not self.__valid_new_author(key, row):
                continue
            self.__set_author(row)

    def __valid_new_author(self, key, row):
        if key == 0 and row[0] == "name":
            return False
        return True

    def __set_author(self, row):
        with contextlib.suppress(IndexError):
            name = row[0]
            self.__authors.append({
                "name": name
            })

    def __list_authors(self):
        for author in self.__authors:
            self.__create_author_or_continue(author)

    def __create_author_or_continue(self, author):
        try:
            Author.objects.create(**author)
            message = "%s created" % (author["name"])
        except IntegrityError:
            message = "%s already created" % (author["name"])

        self.stdout.write(message)

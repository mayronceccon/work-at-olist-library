import csv
import contextlib


class FileRead:
    def __init__(self, file):
        self.__data = []
        self.__file = file

    def execute(self):
        self.__open_file(self.__file)

    def get_data(self):
        return self.__data

    def __open_file(self, file_import):
        with open(file_import, newline="") as csvfile:
            self.__read_file(csvfile)

    def __read_file(self, csvfile):
        reader = csv.reader(csvfile, delimiter=";", quotechar='"')
        self.__list_register(reader)

    def __list_register(self, reader):
        keys = []
        for (key, row) in enumerate(reader):
            if self.__first_line(key):
                keys = row
                continue
            self.__set_data(keys, row)

    def __first_line(self, key):
        if key == 0:
            return True
        return False

    def __set_data(self, keys, row):
        with contextlib.suppress(IndexError):
            data = zip(keys, row)
            self.__data.append(dict(data))

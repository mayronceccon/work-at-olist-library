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
        for (key, row) in enumerate(reader):
            if not self.__valid_data(key, row):
                continue
            self.__set_data(row)

    def __valid_data(self, key, row):
        if key == 0 and row[0] == "name":
            return False
        return True

    def __set_data(self, row):
        with contextlib.suppress(IndexError):
            name = row[0]
            self.__data.append({
                "name": name
            })

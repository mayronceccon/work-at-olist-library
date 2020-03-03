from django.db.utils import IntegrityError
from django.db.models import Model


class ImportData:
    def __init__(self, model, data):
        if not isinstance(model(), Model):
            raise TypeError()

        self.__data = data
        self.__model = model
        self.__messages = []

    def execute(self):
        for data in self.__data:
            self.__create_or_continue(data)

    def get_messages(self):
        return self.__messages

    def __create_or_continue(self, data):
        key_dict = data[next(iter(data))]
        try:
            self.__model.objects.create(**data)
            self.__messages.append("%s created" % (key_dict))
        except IntegrityError:
            self.__messages.append("%s already created" % (key_dict))

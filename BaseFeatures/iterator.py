from collections.abc import Iterable, Iterator


class AddedDatabaseOrderIterator(Iterator):

    def __init__(self, qs):
        self.querySet = qs
        self.position = -1

    def __next__(self):
        try:
            value = self.querySet[self.position]
            self.position += -1
        except IndexError:
            raise StopIteration()
        return value


class DatabaseCollection(Iterable):

    def __init__(self, qs):
        self.querySet = qs

    def __iter__(self):
        return AddedDatabaseOrderIterator(self.querySet)


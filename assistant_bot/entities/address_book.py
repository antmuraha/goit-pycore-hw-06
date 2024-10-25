from collections import UserDict
from assistant_bot.entities.record import Record


class AddressBook(UserDict):
    '''
    A class for storing and managing records.
    '''

    def __init__(self):
        self.data = {}

    def __str__(self):
        count = len(self.data)
        return f"Address Book with {count} records"

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        return self.data[name]

    def delete(self, name: str):
        removed_value = self.data.pop(name)
        return removed_value

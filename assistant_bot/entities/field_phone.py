
from assistant_bot.entities.field import Field


class FieldPhone(Field):
    '''
    A class for storing the phone of a contact.
    '''

    def validation(self, value: str) -> str:
        if len(value) != 10:
            raise FieldPhoneValueError

        return value


class FieldPhoneValueError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

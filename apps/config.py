from enum import Enum


class Connectors(Enum):
    AMAZON = "AMAZON"

    def __str__(self):
        return self.value

    @classmethod
    def get_choices(cls):
        return [(item.value, item.value) for item in cls]

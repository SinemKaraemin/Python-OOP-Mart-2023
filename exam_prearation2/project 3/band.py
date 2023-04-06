from typing import List

from exam_preparation.project3.band_members.musician import Musician


class Band:
    def __init__(self, name: str):
        self.name = name
        self.members: List[Musician] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value == '':
            raise ValueError("Band name should contain at least one character!")

        self.__name = value

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."


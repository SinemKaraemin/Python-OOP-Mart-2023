from .booth import Booth


class PrivateBooth(Booth):
    @property
    def get_price_for_one_person(self):
        return 3.50

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * self.get_price_for_one_person
        self.is_reserved = True

from .booth import Booth


class OpenBooth(Booth):
    @property
    def get_price_per_person(self):
        return 2.50

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * self.get_price_per_person
        self.is_reserved = True

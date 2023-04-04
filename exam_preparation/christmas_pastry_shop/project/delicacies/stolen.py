from .delicacy import Delicacy


class Stolen(Delicacy):
    @property
    def get_portion(self):
        return 250

    def __init__(self, name: str, price: float):
        super().__init__(name, self.get_portion, price)

    def details(self):
        return f"Stolen {self.name}: {self.get_portion}g - {self.price:.2f}lv."



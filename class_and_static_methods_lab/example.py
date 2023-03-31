class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def pepperoni(cls):
        return cls(['fsef', 'efwwe', 'fewf'])

    @classmethod
    def formaggi(cls):
        return cls(['fsef', 'efwwe', 'fewf'])


first_pizza = Pizza.pepperoni()
second_pizza = Pizza.formaggi()

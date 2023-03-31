class Person:
    persons_list = []
    person_num = 0

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return self.name + ' ' + self.surname

    def __add__(self, other):
        return self.name + ' ' + other.surname


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __add__(self, other):
        return self.people + other.people

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        persons = ', '.join([str(x) for x in self.people])
        return f"Group {self.name} with members {persons}"


from project1.employee import Employee
from project1.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'

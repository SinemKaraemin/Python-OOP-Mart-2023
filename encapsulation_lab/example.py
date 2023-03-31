class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def info(self):
        print(self.__age)

    def set_age(self, age):
        if age < 0:
            raise ValueError('Age cannot be negative')
        self.__age = age


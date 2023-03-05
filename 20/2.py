from datetime import *
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def new_person(cls, name):
        cls(name, today().datetime)

    @staticmethod
    def is_old_pers(person):
        return person.age >= 18
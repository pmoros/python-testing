from enum import Enum


import enum


class Gender(enum.Enum):
    male = "Male"
    female = "Female"


class Member:
    def __init__(self, id, name, gender):
        self.id = id
        self.name = name
        self.gender = gender
        self.mother = None
        self.father = None
        self.spouse = None
        self.children = []

    def set_mother(self, mother):
        if not isinstance(mother, Member):
            raise TypeError("Invalid value for mother")
        elif mother.gender != Gender.female:
            raise ValueError(
                "Invalid gender value for mother" "Mother should be female"
            )
        else:
            self.mother = mother

    def set_father(self, father):
        if not isinstance(father, Member):
            raise TypeError("Invalid value for father")
        elif father.gender != Gender.male:
            raise ValueError("Invalid gender value for father" "Father should be male")
        else:
            self.father = father

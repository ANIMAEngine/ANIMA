"""
Base Entity
"""

from agents.body import Body
from agents.genetics import Genetics


class Entity:

    _id_counter = 1

    def __init__(
        self,
        name,
        species,
        gender,
        x=0,
        y=0,
    ):

        self.id = Entity._id_counter
        Entity._id_counter += 1

        self.name = name
        self.species = species
        self.gender = gender

        self.age = 0

        self.alive = True

        self.x = x
        self.y = y

        self.body = Body()

        self.genetics = Genetics()

    # -------------------------------------

    def move(self, dx, dy):

        self.x += dx

        self.y += dy

    # -------------------------------------

    def update(self):

        if not self.alive:

            return

        self.body.update()

        if not self.body.alive:

            self.alive = False

    # -------------------------------------

    def __str__(self):

        return (
            f"{self.species} #{self.id}\n"
            f"Name : {self.name}\n"
            f"Age : {self.age}\n"
            f"Gender : {self.gender}\n"
            f"Position : ({self.x},{self.y})\n"
            f"{self.body}\n"
            f"{self.genetics}"
        )
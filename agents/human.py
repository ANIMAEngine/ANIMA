"""
ANIMA Project
Human
"""

import random

from agents.body import Body
from agents.genetics import Genetics
from agents.perception import Perception
from agents.memory import Memory


class Human:

    counter = 1

    male_names = [
        "James",
        "Liam",
        "Noah",
        "Henry",
        "Lucas"
    ]

    female_names = [
        "Sophia",
        "Emma",
        "Olivia",
        "Charlotte",
        "Amelia"
    ]

    def __init__(self, x=0, y=0):

        self.id = Human.counter
        Human.counter += 1

        self.gender = random.choice(["Male", "Female"])

        if self.gender == "Male":
            self.name = random.choice(self.male_names)
        else:
            self.name = random.choice(self.female_names)

        self.age = 0

        self.x = x
        self.y = y

        self.body = Body()

        self.genetics = Genetics()

        self.perception = Perception()

        self.memory = Memory()

    # ------------------------------------------------

    def update(self):

        self.body.update()

    # ------------------------------------------------

    def perceive(self, world):

        return self.perception.scan(self, world)

    # ------------------------------------------------

    def __str__(self):

        return (
            f"Human #{self.id}\n"
            f"Name : {self.name}\n"
            f"Age : {self.age}\n"
            f"Gender : {self.gender}\n"
            f"Position : ({self.x}, {self.y})\n"
            f"{self.body}"
        )
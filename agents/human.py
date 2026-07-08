"""
ANIMA Project

Human Entity
"""

import random

from agents.body import Body
from agents.genetics import Genetics


class Human:

    _next_id = 1

    # -------------------------------------------------

    def __init__(self, x: int, y: int):

        self.id = Human._next_id
        Human._next_id += 1

        # Identity
        self.name = random.choice([
            "Sophia",
            "Liam",
            "Emma",
            "Noah",
            "Olivia",
            "James",
            "Charlotte",
            "Lucas",
            "Amelia",
            "Henry"
        ])

        self.gender = random.choice([
            "Male",
            "Female"
        ])

        self.age = 0

        # Position
        self.x = x
        self.y = y

        # Components
        self.genetics = Genetics()
        self.body = Body()

    # -------------------------------------------------

    @property
    def position(self):

        return (self.x, self.y)

    # -------------------------------------------------

    def update(self):

        self.body.update()

    # -------------------------------------------------

    def __str__(self):

        return (
            f"Human #{self.id}\n"
            f"Name : {self.name}\n"
            f"Age : {self.age}\n"
            f"Gender : {self.gender}\n"
            f"Position : ({self.x}, {self.y})\n"
            f"{self.body}"
        )
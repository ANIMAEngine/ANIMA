"""
ANIMA Project
Body System

Represents the physical state of an entity.
"""


class Body:

    def __init__(self):

        self.max_health = 100
        self.health = 100

        self.max_energy = 100
        self.energy = 100

        self.max_hunger = 100
        self.hunger = 0

        self.max_thirst = 100
        self.thirst = 0

    # ---------------------------------

    def update(self):

        self.hunger += 0.15
        self.thirst += 0.25
        self.energy -= 0.10

        self.hunger = min(self.hunger, self.max_hunger)
        self.thirst = min(self.thirst, self.max_thirst)
        self.energy = max(self.energy, 0)

        if self.hunger >= 100:

            self.health -= 0.10

        if self.thirst >= 100:

            self.health -= 0.30

        self.health = max(self.health, 0)

    # ---------------------------------

    @property
    def alive(self):

        return self.health > 0

    # ---------------------------------

    def __str__(self):

        return (
            f"HP:{self.health:.1f} | "
            f"Energy:{self.energy:.1f} | "
            f"Hunger:{self.hunger:.1f} | "
            f"Thirst:{self.thirst:.1f}"
        )
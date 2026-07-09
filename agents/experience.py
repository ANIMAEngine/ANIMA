"""
ANIMA Project
Experience

Represents one experience of an entity.
"""


class Experience:

    def __init__(
        self,
        year,
        day,
        tick,
        position,
        observation,
    ):

        self.year = year
        self.day = day
        self.tick = tick

        self.position = position

        self.observation = observation

    # -------------------------------------

    def __str__(self):

        return (
            f"[Y{self.year} D{self.day} T{self.tick}] "
            f"{self.position} -> "
            f"{self.observation}"
        )
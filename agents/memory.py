"""
ANIMA Project
Memory System

Stores experiences.
Does NOT analyse them.
"""


class Memory:

    def __init__(self):

        self.experiences = []

    # -------------------------------------

    def add(self, experience):

        self.experiences.append(experience)

    # -------------------------------------

    def latest(self):

        if not self.experiences:
            return None

        return self.experiences[-1]

    # -------------------------------------

    def all(self):

        return self.experiences

    # -------------------------------------

    def clear(self):

        self.experiences.clear()

    # -------------------------------------

    def __len__(self):

        return len(self.experiences)
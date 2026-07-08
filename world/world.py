"""
ANIMA Project
World
"""

from collections import Counter

from world.generator import WorldGenerator
from world.spawn import SpawnSystem


class World:

    def __init__(self):

        self.map = None

        self.humans = []

        self.spawner = SpawnSystem(self)

    # -------------------------------------------------

    def generate(self):

        generator = WorldGenerator()

        self.map = generator.generate()

    # -------------------------------------------------

    def spawn_humans(self, amount):

        print()

        print("Spawning Humans...")

        print()

        for i in range(amount):

            human = self.spawner.spawn_human()

            self.humans.append(human)

            print(
                f"Human #{i + 1} -> ({human.x}, {human.y})"
            )

    def update(self):

        for human in self.humans:
            human.update()

            print(human)

            print()

    def update(self):

        for human in self.humans:
            human.update()

            print(human)
            print()
    # -------------------------------------------------

    def statistics(self):

        counter = Counter()

        for tile in self.map.tiles:

            counter[tile.type.value] += 1

        print()

        print("========== WORLD ==========")

        print()

        print(f"Size : {self.map.width} x {self.map.height}")

        print()

        for name, amount in counter.items():

            print(f"{name:<12} {amount}")

        print()

        print("===========================")
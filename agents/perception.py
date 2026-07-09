"""
ANIMA Project
Perception System

Responsible for sensing the surrounding world.
It only observes.
It never decides.
"""

from collections import Counter


class Perception:

    def __init__(self, vision_radius=5):

        self.vision_radius = vision_radius

        self.visible_tiles = []
        self.visible_humans = []

    # -----------------------------------------

    def scan(self, human, world):

        self.visible_tiles.clear()
        self.visible_humans.clear()

        counter = Counter()

        # Scan nearby tiles
        for tile in world.map.tiles:

            dx = abs(tile.x - human.x)
            dy = abs(tile.y - human.y)

            if dx <= self.vision_radius and dy <= self.vision_radius:

                self.visible_tiles.append(tile)

                counter[tile.type.value] += 1

        # Scan nearby humans
        for other in world.humans:

            if other is human:
                continue

            dx = abs(other.x - human.x)
            dy = abs(other.y - human.y)

            if dx <= self.vision_radius and dy <= self.vision_radius:

                self.visible_humans.append(other)

        return {
            "tiles": dict(counter),
            "humans": len(self.visible_humans)
        }
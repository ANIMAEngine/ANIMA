"""
ANIMA Project

Spawn System
"""

import random

from agents.human import Human

from world.tile_types import TileType


class SpawnSystem:

    def __init__(self, world):

        self.world = world

    # -----------------------------------------

    def spawn_human(self):

        while True:

            x = random.randint(0, self.world.map.width - 1)

            y = random.randint(0, self.world.map.height - 1)

            tile = self.world.map.get_tile(x, y)

            if tile.type in (

                TileType.GRASS,

                TileType.FOREST,

            ):

                return Human(x=x, y=y)
"""
ANIMA Project
World Generator
"""

import random

from world.map import WorldMap
from world.tile import Tile
from world.tile_types import TileType


class WorldGenerator:

    def __init__(self, width=100, height=100):

        self.width = width

        self.height = height

    # -------------------------------------------------

    def generate(self):

        world = WorldMap(self.width, self.height)

        terrain = [

            TileType.GRASS,
            TileType.GRASS,
            TileType.GRASS,
            TileType.GRASS,

            TileType.FOREST,
            TileType.FOREST,

            TileType.WATER,
            TileType.WATER,

            TileType.MOUNTAIN,

            TileType.SAND

        ]

        for y in range(self.height):

            for x in range(self.width):

                tile = Tile(

                    x,

                    y,

                    random.choice(terrain)

                )

                world.add_tile(tile)

        return world
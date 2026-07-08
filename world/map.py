"""
ANIMA Project
Map

Stores every tile inside the world.
"""

from world.tile import Tile


class WorldMap:

    def __init__(self, width: int, height: int):

        self.width = width

        self.height = height

        self.tiles = []

    # -------------------------------------------------

    def add_tile(self, tile: Tile):

        self.tiles.append(tile)

    # -------------------------------------------------

    def get_tile(self, x: int, y: int):

        index = y * self.width + x

        return self.tiles[index]

    # -------------------------------------------------

    @property
    def size(self):

        return len(self.tiles)
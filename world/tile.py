"""
ANIMA Project
Tile

Represents a single cell of the world map.
"""

from world.tile_types import TileType


class Tile:

    def __init__(
        self,
        x: int,
        y: int,
        tile_type: TileType,
    ):

        self.x = x

        self.y = y

        self.type = tile_type

        self.walkable = tile_type != TileType.WATER

        self.movement_cost = self._movement_cost()

    # -------------------------------------------------

    def _movement_cost(self):

        if self.type == TileType.GRASS:
            return 1

        if self.type == TileType.FOREST:
            return 2

        if self.type == TileType.HILL:
            return 2

        if self.type == TileType.SAND:
            return 3

        if self.type == TileType.SWAMP:
            return 4

        if self.type == TileType.MOUNTAIN:
            return 5

        return 999

    # -------------------------------------------------

    def __str__(self):

        return f"{self.type.value} ({self.x}, {self.y})"
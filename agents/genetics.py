"""
ANIMA Project
Genetics System
"""

import random


class Genetics:

    def __init__(self):

        self.height = random.randint(150, 195)

        self.strength = random.randint(1, 10)

        self.intelligence = random.randint(1, 10)

        self.speed = random.randint(1, 10)

        self.endurance = random.randint(1, 10)

    def __str__(self):

        return (
            f"Height:{self.height} "
            f"STR:{self.strength} "
            f"INT:{self.intelligence} "
            f"SPD:{self.speed} "
            f"END:{self.endurance}"
        )
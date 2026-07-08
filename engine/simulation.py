"""
ANIMA Project

Simulation Engine
"""

import time


class Simulation:

    def __init__(self, world, clock):

        self.world = world
        self.clock = clock
        self.running = False

    # -----------------------------------------

    def start(self, ticks=10):

        self.running = True

        print("\nSimulation Started\n")

        while self.running and self.clock.tick < ticks:

            self.clock.update()

            print("=" * 40)
            print(self.clock)
            print("=" * 40)

            self.world.update()

            time.sleep(0.5)

        print("\nSimulation Finished.")
from engine.clock import Clock
from engine.simulation import Simulation
from world.world import World


def main():

    clock = Clock()

    world = World()

    world.generate()

    world.statistics()

    world.spawn_humans(5)

    simulation = Simulation(world, clock)

    simulation.start(5)


if __name__ == "__main__":
    main()
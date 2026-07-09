from world.world import World

from agents.experience import Experience


def main():

    world = World()

    world.generate()

    world.statistics()

    world.spawn_humans(5)

    print()
    print("===== PERCEPTION TEST =====")
    print()

    for human in world.humans:

        print("=" * 40)

        print(human)

        observation = human.perceive(world)

        experience = Experience(

            year=1,
            day=1,
            tick=0,

            position=(human.x, human.y),

            observation=observation

        )

        human.memory.add(experience)

        print()

        print("Visible World")

        print(observation)

        print()

        print("Latest Memory")

        print(human.memory.latest())

        print()


if __name__ == "__main__":
    main()
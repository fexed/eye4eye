from environment.environment import Environment, DebugLevel
from actors.randomActor import RandomActor
from actors.cooperator import Cooperator
from actors.defector import Defector
from actors.titForTatActor import TitForTatActor


def main():
    print("eye4eye alpha v0.0.1")
    
    env = Environment(DEBUG_LEVEL = DebugLevel.MATCH)

    env.add_actor(RandomActor(1))
    env.add_actor(Cooperator(2))
    env.add_actor(Defector(3))
    env.add_actor(TitForTatActor(4))
    env.play()


if __name__ == "__main__":
    main()
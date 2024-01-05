from environment.environment import Environment, DebugLevel
from actors.randomActor import RandomActor
from actors.cooperator import Cooperator
from actors.defector import Defector
from actors.titForTatActor import TitForTatActor


def main():
    print("eye4eye alpha v0.0.1")
    
    env = Environment(DEBUG_LEVEL = DebugLevel.MATCH)

    act = RandomActor()
    act.name = "rndm"
    env.add_actor(act)

    act = Cooperator()
    act.name = "coop"
    env.add_actor(act)
    
    act = Defector()
    act.name = "dfct"
    env.add_actor(act)
    
    act = TitForTatActor()
    act.name = "tfta"
    env.add_actor(act)
    env.play()


if __name__ == "__main__":
    main()
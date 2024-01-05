from Environment import Environment
from RandomActor import RandomActor
from Cooperator import Cooperator
from Defector import Defector
from TitForTatActor import TitForTatActor


def main():
    print("eye4eye alpha v0.0.1")
    
    env = Environment()
    env.DEBUG_OUTPUT = True

    env.add_actor(RandomActor(1))
    env.add_actor(Cooperator(2))
    env.add_actor(Defector(3))
    env.add_actor(TitForTatActor(4))
    env.play()

if __name__ == "__main__":
    main()
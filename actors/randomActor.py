from environment.actor import Actor
from environment.action import Action
import random


class RandomActor(Actor):
    def __init__(self, ix: int = 0):
        super().__init__(ix)
        self.name = "Random actor " + str(ix)

    def choose_action(self):
        self.action = random.choice([Action.COOPERATE, Action.DEFECT])
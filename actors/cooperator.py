from environment.actor import Actor
from environment.action import Action


class Cooperator(Actor):
    def __init__(self, ix: int = 0):
        super().__init__(ix)
        self.name = "Cooperator " + str(ix)


    def choose_action(self):
        self.action = Action.COOPERATE
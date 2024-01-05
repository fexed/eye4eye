from Actor import Actor
from Action import Action


class Defector(Actor):
    def __init__(self, ix: int = 0):
        super().__init__(ix)
        self.name = "Defector " + str(ix)


    def choose_action(self):
        self.action = Action.DEFECT
from environment.actor import Actor
from environment.action import Action


class TitForTatActor(Actor):
    previous_action: Action


    def __init__(self, ix: int = 0):
        super().__init__(ix)
        self.name = "Tit for Tat " + str(ix)
        self.previous_action = Action.UNDEFINED


    def choose_action(self):
        if (self.previous_action == Action.DEFECT):
            self.action = Action.DEFECT
        else:
            self.action = Action.COOPERATE
    
    def result(self, delta_points: int, other_actor_action: Action):
        super().result(delta_points, other_actor_action)
        self.previous_action = other_actor_action
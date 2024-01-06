from environment.actor import Actor
from environment.action import Action


class TitFor2TatsActor(Actor):
    previous_action: Action
    consecutive_defects: int


    def __init__(self, ix: int = 0):
        super().__init__(ix)
        self.name = "Tit for 2 Tats " + str(ix)
        self.previous_action = Action.UNDEFINED
        self.consecutive_defects = 0


    def choose_action(self):
        if (self.previous_action == Action.DEFECT):
            self.consecutive_defects += 1
        else:
            self.consecutive_defects = 0

        if (self.consecutive_defects >= 2):
            self.action = Action.DEFECT
        else:
            self.action = Action.COOPERATE


    def result(self, delta_points: int, other_actor_action: Action):
        super().result(delta_points, other_actor_action)
        self.previous_action = other_actor_action
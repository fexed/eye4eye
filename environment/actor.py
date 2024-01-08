from environment.action import Action


class Actor:
    name: str
    points: int
    action: Action
    played: int


    def __init__(self, ix: int = 0):
        self.name = "Undefined actor " + str(ix)
        self.points = 0
        self.played = 0
        self.action = Action.UNDEFINED


    def choose_action(self):
        self.action = Action.UNDEFINED


    def result(self, delta_points: int, other_actor_action: Action):
        self.points += delta_points
        self.played += 1

    
    def print_status(self):
        print(self.name + " has " + str(self.points/self.played) + " points per match")

    
    def reset(self):
        self.action = Action.UNDEFINED
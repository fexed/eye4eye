from environment.action import Action


class Actor:
    name: str
    points: int
    action: Action


    def __init__(self, ix: int = 0):
        self.name = "Undefined actor " + str(ix)
        self.points = 0
        self.action = Action.UNDEFINED


    def choose_action(self):
        self.action = Action.UNDEFINED


    def result(self, delta_points: int, other_actor_action: Action):
        self.points += delta_points

    
    def print_status(self):
        print(self.name + " has " + str(self.points) + " points")

    
    def reset(self):
        self.points = 0
        self.action = Action.UNDEFINED
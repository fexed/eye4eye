from environment.actor import Actor
from environment.action import Action
import random


class RLActor(Actor):
    cooperate_prob: float
    iteration: int

    def __init__(self, ix: int = 0):
        super().__init__(ix)
        self.name = "RL Actor " + str(ix)
        self.cooperate_prob = 0.5
        self.iteration = 0


    def choose_action(self):
        self.action = random.choices(
            population = [Action.COOPERATE, Action.DEFECT],
            weights = [self.cooperate_prob, 1 - self.cooperate_prob],
            k = 1
        )[0]


    def result(self, delta_points: int, other_actor_action: Action):
        super().result(delta_points, other_actor_action)
        if (self.action == Action.COOPERATE):
            if (delta_points < 0):
                self.cooperate_prob -= 0.01
                self.cooperate_prob = max(self.cooperate_prob, 0.01)
            else:
                self.cooperate_prob += 0.01
                self.cooperate_prob = min(self.cooperate_prob, 0.99)
        elif (self.action == Action.DEFECT):
            if (delta_points < 0):
                self.cooperate_prob += 0.01
                self.cooperate_prob = min(self.cooperate_prob, 0.99)
            else:
                self.cooperate_prob -= 0.01
                self.cooperate_prob = max(self.cooperate_prob, 0.01)

    
    def print_status(self):
        print(self.name + " has " + str(self.points) + " points, p = " + str(self.cooperate_prob))

    
    def reset(self):
        super().reset()
        self.iteration = 0
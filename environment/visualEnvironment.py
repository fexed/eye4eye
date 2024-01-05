from environment.environment import Environment, DebugLevel
from environment.action import Action
from environment.actor import Actor
import os
import math

class VisualEnvironment(Environment):
    i: int = 0
    curr_x: int = 0
    curr_y: int = 0
    indexes = {}


    def print_char(self, x, y, char):
        print("\033["+str(y)+";"+str(x)+"H"+char, end="")


    def __init__(self, DEBUG_LEVEL: DebugLevel = DebugLevel.NO_DEBUG):
        super().__init__(DEBUG_LEVEL)
        self.DEBUG_LEVEL = DebugLevel.NO_DEBUG


    def pre_play(self):
        super().pre_play()
        os.system('cls' if os.name == 'nt' else 'clear')
        for ix, actor in enumerate(self.actors):
            self.print_char(0, ix + 2, actor.name)
            self.indexes[actor.name] = ix + 2
            if (len(actor.name) > self.curr_x): self.curr_x = len(actor.name)
        self.curr_x += 2


    def pre_round(self):
        super().pre_round()
        self.print_char(self.curr_x, 0, str(self.i + 1))
        self.i += 1

    
    def post_round(self):
        super().post_round()
        for ix, actor in enumerate(self.actors):
            label = "C" if actor.action == Action.COOPERATE else ("D" if actor.action == Action.DEFECT else "U")
            self.print_char(self.curr_x, ix + 2, label)
        self.curr_x += int(math.log10(self.i)) + 2
        
    
    def post_play(self):
        super().post_play()
        print("\n")
        self.print_status()


    def post_match(self, first: Actor, second: Actor):
        super().post_match(first, second)
        

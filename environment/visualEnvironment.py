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
        ix = 0
        curr_pair = 0
        for actor in self.actors:
            self.indexes[actor.name] = ix + 3
            if curr_pair == 2: 
                self.indexes[actor.name] += 1
                ix += 1
                curr_pair = 0
            curr_pair += 1
            self.print_char(0, self.indexes[actor.name], actor.name)
            if (len(actor.name) > self.curr_x): self.curr_x = len(actor.name)
            ix += 1
        self.curr_x += 2


    def pre_round(self):
        super().pre_round()
        self.print_char(self.curr_x, 0, str(self.i + 1))
        self.print_char(self.curr_x, 2, "-")
        self.i += 1

    
    def post_round(self):
        super().post_round()
        self.curr_x += int(math.log10(self.i)) + 3
        
    
    def post_play(self):
        super().post_play()
        self.print_char(0, len(self.actors) + (math.log2(len(self.actors))), "\n\n\n\n")
        self.print_status()


    def post_match(self, first: Actor, second: Actor):
        super().post_match(first, second)
        label = "C" if first.action == Action.COOPERATE else ("D" if first.action == Action.DEFECT else "U")
        self.print_char(self.curr_x, self.indexes[first.name], label)
        label = "C" if second.action == Action.COOPERATE else ("D" if second.action == Action.DEFECT else "U")
        self.print_char(self.curr_x, self.indexes[second.name], label)
        

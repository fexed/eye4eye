from environment.actor import Actor
from environment.action import Action
from enum import Enum
from functools import total_ordering
import time
import random


MAX_ROUNDS = 500


@total_ordering
class DebugLevel(Enum):
    NO_DEBUG = -1
    RUN = 0
    ROUND = 1
    MATCH = 2

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

class Environment:
    actors: [Actor]
    DEBUG_LEVEL: DebugLevel = DebugLevel.NO_DEBUG


    def __init__(self, DEBUG_LEVEL: DebugLevel = DebugLevel.NO_DEBUG):
        self.actors = []
        self.DEBUG_LEVEL = DEBUG_LEVEL
    

    def add_actor(self, actor: Actor):
        self.actors.append(actor)
        if (self.DEBUG_LEVEL >= DebugLevel.RUN): print("ENVDBG\tAdding actor " + actor.name + " to environment")

    
    def play(self):
        random.shuffle(self.actors)
        num_rounds = random.randint(MAX_ROUNDS, MAX_ROUNDS)
        if (self.DEBUG_LEVEL >= DebugLevel.RUN):
            print("About to play " + str(num_rounds) + " rounds with " + str(len(self.actors)) + " actors\n")
            start_time = time.time()

        for i in range(0, num_rounds):
            if (self.DEBUG_LEVEL >= DebugLevel.ROUND): print("RNDDBG\tRound " + str(i + 1))
            match_played, points_delta = self.play_round(is_first_round = (i == 0))
            if (self.DEBUG_LEVEL >= DebugLevel.ROUND): print("RNDDBG\t" + str(match_played) + " matches for a delta of " + str(points_delta) + " points\n")
        
        if (self.DEBUG_LEVEL >= DebugLevel.RUN):
            end_time = time.time()
            print("\nRUNDBG\tPlayed " + str(num_rounds) + " rounds in " + str((end_time - start_time) * 1000) + " ms")
            self.print_status()


    def play_round(self, is_first_round: bool = False):
        match_played, points_delta = 0, 0
        for first, second in zip(self.actors, self.actors[1:]):
            if (self.DEBUG_LEVEL >= DebugLevel.MATCH): print("MTCDBG\tFacing off " + first.name + " vs " + second.name)
            first.choose_action()
            second.choose_action()
            (first_reward, second_reward) = self.play_match(first.action, second.action)
            if (self.DEBUG_LEVEL >= DebugLevel.MATCH): print("MTCDBG\t" + str(first.action) + " vs " + str(second.action))
            first.result(first_reward, other_actor_action = second.action)
            second.result(second_reward, other_actor_action = first.action)

            match_played += 1
            points_delta += abs(first_reward) + abs(second_reward)
        return (match_played, points_delta)


    def play_match(self, first_action: Action, second_action: Action):
        first_reward = 0
        second_reward = 0

        if (first_action == Action.COOPERATE):
            if (second_action == Action.COOPERATE):
                first_reward = 3
                second_reward = 3
                return (first_reward, second_reward)
            elif (second_action == Action.DEFECT):
                first_reward = 0
                second_reward = 5
                return (first_reward, second_reward)
        elif (first_action == Action.DEFECT):
            if (second_action == Action.COOPERATE):
                first_reward = 5
                second_reward = 0
                return (first_reward, second_reward)
            elif (second_action == Action.DEFECT):
                first_reward = 1
                second_reward = 1
                return (first_reward, second_reward)
              
        return (first_reward, second_reward)


    def print_status(self):
        top_players = sorted(self.actors, key = lambda actor : actor.points, reverse = True)
        for actor in top_players:
            actor.print_status()
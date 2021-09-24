from bot import Bot
from constants import *
from random import randint


class AlexBot(Bot):
    def __init__(self):
        self.move = ''
        self.dynamite = 0
        self.counter = 0
        pass

    def make_move(self, gamestate):
        move_index = randint(0, 2)
        self.move = VALID_MOVES[move_index]
        if self.counter > ROUND_LIMIT * 0.7:
            random = randint(0, 1)
            if random == 0:
                self.move = 'D'
                self.dynamite += 1
            else:
                self.move = VALID_MOVES[move_index]
            if self.dynamite >= NUM_DYNAMITE:
                self.move = VALID_MOVES[move_index]
        self.counter += 1
        return self.move

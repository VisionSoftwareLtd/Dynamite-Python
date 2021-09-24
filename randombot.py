import random

from bot import Bot


class RandomBot(Bot):
  def __init__(self):
    random.seed()

  def make_move(self, gamestate):
    choice = self.__randomChoice()
    return choice

  def __randomChoice(self):
    rps = ['R', 'P', 'S']
    choice = random.choice(rps)
    return choice

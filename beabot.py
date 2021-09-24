from bot import Bot
import random


class BeaBot(Bot):
  def __init__(self):
    pass

  def make_move(self, gamestate):
    options = ['R', 'S', 'P', 'W',]
    output = options[random.randint(0, len(options) - 1)]
    return output
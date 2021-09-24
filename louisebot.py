import random
from paperbot import PaperBot as bot1
# from rockbot import RockBot as bot2

from bot import Bot

variables = ['D', 'W', 'R', 'S', 'P']

class LouiseDBot(Bot):

  def __init__(self):
    pass

  def make_move(self, gamestate):
      variables = ['D', 'W', 'R', 'S', 'P']
      return random.choice(variables)






    # if bot2 == 'P':
    #   return 'S'
    # elif bot2 == 'R':
    #   return 'P'
    # elif bot2 == 'S':
    #   return 'R'
    # elif bot2 == 'D':
    #   return 'W'
    # elif bot2 == 'W':
    #   return 'S'
    # else:
    #   return random.choice(variables)


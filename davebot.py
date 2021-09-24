import random
from constants import *
from bot import Bot

class DaveBot(Bot):
  def __init__(self):
    random.seed()
    self.__numDynamite = NUM_DYNAMITE
    self.__numDrawsNeededForDynamite = random.randint(2, 4)

  def make_move(self, gamestate):
    enemyMoveCount = {}
    for move in VALID_MOVES:
      enemyMoveCount[move] = 0
    for state in gamestate['rounds']:
      enemyMoveCount[state['p2']] += 1
    numRoundsPlayed = len(gamestate['rounds'])
    if enemyMoveCount['R'] > numRoundsPlayed / 2:
      choice = 'P'
    elif enemyMoveCount['P'] > numRoundsPlayed / 2:
      choice = 'S'
    elif enemyMoveCount['S'] > numRoundsPlayed / 2:
      choice = 'R'
    elif self.__shouldPlayDynamite(gamestate['rounds']):
      choice = 'D'
    else:
      choice = self.__randomChoice()
    return choice

  def __randomChoice(self):
    rps = ['R', 'P', 'S']
    choice = random.choice(rps)
    return choice

  def __shouldPlayDynamite(self, rounds):
    roundsTrimmed = rounds[-self.__numDrawsNeededForDynamite:]
    for roundCheck in roundsTrimmed:
      if roundCheck['p1'] != roundCheck['p2']:
        return False
    self.__numDynamite -= 1
    self.__numDrawsNeededForDynamite = random.randint(2, 4)
    return self.__numDynamite >= 0

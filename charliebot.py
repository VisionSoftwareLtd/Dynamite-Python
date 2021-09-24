from bot import Bot
import random
import constants
from game import *






class CharlieBot(Bot):
  def __init__(self):
    self.__dynamite_use = 0

  def make_move(self, gamestate):
    move=random.choice(VALID_MOVES)
    reading=gamestate['rounds']

    #counting moves
    s_counter = 0
    r_counter = 0
    p_counter = 0
    d_counter = 0
    w_counter = 0
    for state in reading:
      for status in state:
        #print(state[status])
        if state[status] == 'S':
          s_counter +=1
        if state[status] == 'R':
          r_counter +=1
        if state[status] == 'P':
          p_counter +=1
        if state[status] == 'D':
          d_counter +=1
        if state[status] == 'W':
          w_counter += 1
        #print(s_counter, d_counter, r_counter, p_counter, w_counter)
    # find the most common move
    total_plays = s_counter + d_counter + r_counter + p_counter + w_counter
    if move =='D':
      self.__dynamite_use = self.__dynamite_use+1
      if self.__dynamite_use >= 100: #limiting dynamite use
        move = 'R'
      #print(self.__dynamite_use)
    if move == 'W':
      print('Water Fight!')
    return move

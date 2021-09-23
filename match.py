from game import Game

class Match:
  def __init__(self, bot1, bot2):
    self.__bots = [bot1, bot2]
    self.__result = {}

  def play(self):
    self.__result = Game(self.__bots[0], self.__bots[1]).play()

  def getResult(self):
    return self.__result

  def __eq__(self, other):
    return ((self.__bots[0] == other.__bots[0] and self.__bots[1] == other.__bots[1]) or
            (self.__bots[0] == other.__bots[1] and self.__bots[1] == other.__bots[0]))

  def __str__(self):
    vsText = f'{self.__bots[0].__class__.__name__} vs {self.__bots[1].__class__.__name__}'
    if self.__result == {}:
      return vsText
    elif self.__result['reason'] == 'score':
      winner = self.__result['winner']
      winnerName = self.__bots[winner].__class__.__name__
      scoreText = f"{self.__result['score'][winner]} against {self.__result['score'][1 - winner]}"
      return f'{vsText} : {winnerName} wins with a score of {scoreText}'
    elif self.__result['reason'] == 'round limit':
      return f"{vsText} : It's a draw!"
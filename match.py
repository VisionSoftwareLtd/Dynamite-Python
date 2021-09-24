from game import Game

class Match:
  def __init__(self, bot1, bot2):
    self.__bots = [bot1, bot2]
    self.__result = {}

  def getBot(self, botNumber):
    return self.__bots[botNumber]

  def play(self):
    for bot in self.__bots:
      bot.__init__()
    self.__result = Game(self.__bots[0], self.__bots[1]).play()

  def getResult(self):
    return self.__result

  def getVsText(self):
    return f'{str(self.__bots[0]):^15} vs {str(self.__bots[1]):^15}'

  def __eq__(self, other):
    return ((self.__bots[0] == other.__bots[0] and self.__bots[1] == other.__bots[1]) or
            (self.__bots[0] == other.__bots[1] and self.__bots[1] == other.__bots[0]))

  def __str__(self):
    vsText = self.getVsText()
    if self.__result == {}:
      return vsText
    elif self.__result['reason'] == 'score':
      winner = self.__result['winner']
      winnerBot = self.__bots[winner]
      scoreText = f"{self.__result['score'][winner]} against {self.__result['score'][1 - winner]}"
      return f'{str(winnerBot):<15} wins with a score of {scoreText}'
    elif self.__result['reason'] == 'round limit':
      return f"It's a draw!"

  def getWinner(self):
    if self.__result.get('reason') is None or self.__result['reason'] != 'score':
      return None
    return self.__bots[self.__result['winner']]
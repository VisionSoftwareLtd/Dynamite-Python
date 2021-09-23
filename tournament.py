from match import Match

class Tournament:
  __bots = []

  def addBot(self, bot):
    self.__bots.append(bot)

  def play(self):
    matches = []
    for i in range(len(self.__bots)):
      for j in range(1, len(self.__bots)):
        if i == j:
          continue
        matchToPlay = Match(self.__bots[i], self.__bots[j])
        if matches.__contains__(matchToPlay):
          continue
        matches.append(matchToPlay)

    for match in matches:
      match.play()
      print(match)
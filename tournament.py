from match import Match
import time

class Tournament:
  __bots = []

  def addBot(self, bot):
    self.__bots.append(bot)

  def play(self):
    matches = []
    for i in range(len(self.__bots)):
      for j in range(len(self.__bots)):
        if i == j:
          continue
        matchToPlay = Match(self.__bots[i], self.__bots[j])
        if matches.__contains__(matchToPlay):
          continue
        matches.append(matchToPlay)

    self.__playMatches(matches)
    print()
    self.__printFinalScores(matches)

  def __playMatches(self, matches):
    print('After each match, press ENTER to play next match')
    for count in range(len(matches)):
      match = matches[count]
      print(f'Match {count+1} of {len(matches)} - {match.getVsText()} : ', end='')
      time.sleep(1)
      for i in range(3):
        time.sleep(0.5)
        print('.', end='')
      match.play()
      print(match, end='')
      input()

  def __printFinalScores(self, matches):
    print('Final scores:')
    finalScores = {}
    for bot in self.__bots:
      finalScores[bot] = self.__countWins(bot, matches)
    for bot in finalScores:
      print(f'{bot} : {finalScores[bot]}')

  def __countWins(self, bot, matches):
    count = 0
    for match in matches:
      if match.getWinner() == bot:
        count += 1
    return count

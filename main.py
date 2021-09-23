from paperbot import PaperBot
from rockbot import RockBot
from scissorsbot import ScissorsBot
from tournament import Tournament

def main():
  tournament = Tournament()
  tournament.addBot(PaperBot())
  tournament.addBot(RockBot())
  tournament.addBot(ScissorsBot())
  tournament.play()

if __name__ == '__main__':
  main()
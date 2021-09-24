from alexbot import AlexBot
from beabot import BeaBot
from charliebot import CharlieBot
from danbot import DanBot
from davebot import DaveBot
from harrybot import HarryBot
from louisebot import LouiseDBot
from paperbot import PaperBot
from rajbot import RajBot
from randombot import RandomBot
from tournament import Tournament
from trystanbot import TrystanBot


def main():
  tournament = Tournament()
  tournament.addBot(PaperBot())
  tournament.addBot(RandomBot())
  tournament.addBot(AlexBot())
  tournament.addBot(BeaBot())
  tournament.addBot(CharlieBot())
  tournament.addBot(DanBot())
  tournament.addBot(DaveBot())
  tournament.addBot(HarryBot())
  tournament.addBot(LouiseDBot())
  tournament.addBot(RajBot())
  tournament.addBot(TrystanBot())
  tournament.play()

if __name__ == '__main__':
  main()
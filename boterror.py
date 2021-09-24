class BotError(RuntimeError):
  def __init__(self, playerNum, errorString):
    self.playerNum = playerNum
    self.errorString = errorString
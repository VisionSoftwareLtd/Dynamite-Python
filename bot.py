from abc import ABC, abstractmethod

class Bot(ABC):
  @abstractmethod
  def make_move(self, gamestate):
    raise NotImplementedError('Cannot call base class')

  def __str__(self):
    return self.__class__.__name__
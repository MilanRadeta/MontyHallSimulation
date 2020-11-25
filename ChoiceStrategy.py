import random

class ChoiceStrategy(object):
    def __init__(self, game):
        self.name = self.__class__.__name__
        self.game = game
    
    def __str__(self):
        return self.name

class RandomStrategy(ChoiceStrategy):
    def chooseDoor(self):
        return random.choice(self.game.closedDoors)

class KeepStrategy(RandomStrategy):
    def chooseDoor(self):
        return self.game.chosenDoor or RandomStrategy.chooseDoor(self)

class SwitchStrategy(ChoiceStrategy):
    def chooseDoor(self):
        return random.choice([door for door in self.game.closedDoors if door != self.game.chosenDoor])

class KeepAndSwitchStrategy(SwitchStrategy):
    def chooseDoor(self):
        return self.game.chosenDoor if (self.game.chosenDoor is not None and len(self.game.closedDoors) > 2) else SwitchStrategy.chooseDoor(self)

AllStrategies = [RandomStrategy, KeepStrategy, SwitchStrategy, KeepAndSwitchStrategy]
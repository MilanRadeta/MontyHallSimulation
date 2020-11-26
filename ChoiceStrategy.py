import random


class ChoiceStrategy(object):
    def __init__(self, game):
        self.game = game

    def __str__(self):
        return self.__class__.__name__


class Random(ChoiceStrategy):
    def chooseDoor(self):
        return random.choice(self.game.closedDoors)


class Keep(Random):
    def chooseDoor(self):
        return self.game.chosenDoor or Random.chooseDoor(self)


class Switch(ChoiceStrategy):
    def chooseDoor(self):
        return random.choice([door for door in self.game.closedDoors if door != self.game.chosenDoor])


class OneSwitch(Switch):
    def chooseDoor(self):
        return self.game.chosenDoor if (self.game.chosenDoor is not None and len(self.game.closedDoors) > 2) else Switch.chooseDoor(self)


AllStrategies = [Random, Keep,
                 Switch, OneSwitch]

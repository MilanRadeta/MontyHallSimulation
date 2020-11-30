import random


class ChoiceStrategy(object):
    def __init__(self, game):
        self.game = game

    def chooseDoor(self):
        pass

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


class SwitchOnce(Switch):
    def chooseDoor(self):
        return self.game.chosenDoor if (self.game.chosenDoor is not None and len(self.game.closedDoors) > 2) else Switch.chooseDoor(self)


class FirstDoor(Random):
    def chooseDoor(self):
        return self.game.closedDoors[0]


class RandomNonChosenEmptyClosed(ChoiceStrategy):
    def chooseDoor(self):
        doors = [door for door in self.game.closedDoors if door !=
                 self.game.chosenDoor and not door.hasReward]
        return random.choice(doors)


class RandomClosedOrReward(ChoiceStrategy):
    def chooseDoor(self):
        return self.game.rewardDoor or random.choice(self.game.closedDoors)


class RandomClosed(ChoiceStrategy):
    def chooseDoor(self):
        return random.choice(self.game.closedDoors)


class NoDoor(ChoiceStrategy):
    def chooseDoor(self):
        return None


CommonStrategies = [Random, Keep,
                    Switch, SwitchOnce]

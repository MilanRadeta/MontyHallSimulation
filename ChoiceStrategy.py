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

class RandomClosed(ChoiceStrategy):
    def chooseDoor(self):
        doors = self.game.getAvailableEmptyClosedDoors()
        return random.choice(doors)


class LastClosedDoor(ChoiceStrategy):
    def chooseDoor(self):
        index = -1
        door = None
        while door is None or door.hasReward or door == self.game.chosenDoor:
            door = self.game.closedDoors[index]
            index -= 1
        
        return door


class PreviouslyChosenDoor(ChoiceStrategy):
    def chooseDoor(self):
        return self.game.chosenDoors[-2] if len(self.game.chosenDoors) > 2 and self.game.chosenDoors[-2] != self.game.chosenDoor else Random.chooseDoor(self)


CommonStrategies = [Random, Keep,
                 Switch, SwitchOnce]

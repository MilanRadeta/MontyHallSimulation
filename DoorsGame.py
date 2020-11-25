import random
from ChoiceStrategy import ChoiceStrategy
from Config import Config
from GameResult import GameResult
from Door import Door


class DoorsGame(object):
    def __init__(self, config: Config):
        self.config = config
        self.choiceStrategy: ChoiceStrategy = config.strategy(self)
        self.openDoors = []
        self.doors = [Door(i) for i in range(config.totalDoors)]
        self.closedDoors = self.doors.copy()
        self.setRewardDoor()
        self.emptyDoors = [door for door in self.doors if not door.hasReward]
        self.emptyClosedDoors = [door for door in self.emptyDoors]
        self.chosenDoor = None
        self.chosenDoors = []

    def getRandomClosedDoor(self):
        return random.choice(self.closedDoors)

    def getAvailableEmptyClosedDoors(self):
        if self.chosenDoor is None:
            raise Exception('A door must be chosen first')
        return [door for door in self.emptyClosedDoors if door != self.chosenDoor]

    def getRandomEmptyClosedDoor(self):
        doors = self.getAvailableEmptyClosedDoors()
        return random.choice(doors)

    def setRewardDoor(self):
        self.rewardDoor = self.getRandomClosedDoor()
        self.rewardDoor.hasReward = True

    def openClosedEmptyDoor(self):
        door = self.getRandomEmptyClosedDoor()
        self.openDoor(door)

    def openDoor(self, door: Door):
        door.isOpen = True
        if door in self.emptyClosedDoors:
            self.emptyClosedDoors.remove(door)
        if door in self.closedDoors:
            self.closedDoors.remove(door)
        self.openDoors.append(door)

    def chooseDoor(self, index=None):
        if index is None:
            self.chosenDoor = self.choiceStrategy.chooseDoor()
            self.chosenDoors.append(self.chosenDoor)
            return

        if index >= len(self.doors) or index < 0:
            raise ValueError('Chosen door does not exist')
        if self.doors[index].isOpen:
            raise ValueError('Chosen door is already open')
        self.chosenDoor = self.doors[index]
        self.chosenDoors.append(self.chosenDoor)

    def runGame(self):
        self.chooseDoor()
        while(len(self.closedDoors) > 2):
            self.openClosedEmptyDoor()
            self.chooseDoor()

        self.openDoor(self.chosenDoor)
        self.openDoor(self.closedDoors[0])

        return GameResult(self)

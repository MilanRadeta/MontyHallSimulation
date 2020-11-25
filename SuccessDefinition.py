class SuccessDefinition(object):
    def __init__(self, game):
        self.game = game
    
    def __str__(self):
        return self.__class__.__name__

class RewardDoorSuccessDefinition(SuccessDefinition):
    def hasWon(self):
        return self.game.chosenDoor == self.game.rewardDoor

class NonRewardDoorSuccessDefinition(SuccessDefinition):
    def hasWon(self):
        return self.game.chosenDoor != self.game.rewardDoor

class FirstDoorRewardDoorSuccessDefinition(SuccessDefinition):
    def hasWon(self):
        return self.game.chosenDoors[0] == self.game.rewardDoor

class FirstDoorNonRewardDoorSuccessDefinition(SuccessDefinition):
    def hasWon(self):
        return self.game.chosenDoors[0] != self.game.rewardDoor

AllDefinitions = [RewardDoorSuccessDefinition, NonRewardDoorSuccessDefinition, FirstDoorRewardDoorSuccessDefinition, FirstDoorNonRewardDoorSuccessDefinition]
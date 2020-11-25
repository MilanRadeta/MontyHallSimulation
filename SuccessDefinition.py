class SuccessDefinition():
    def hasWon(game):
        return False


class RewardDoor(SuccessDefinition):
    def hasWon(game):
        return game.chosenDoor == game.rewardDoor


class NonRewardDoor(SuccessDefinition):
    def hasWon(game):
        return game.chosenDoor != game.rewardDoor


class FirstDoorReward(SuccessDefinition):
    def hasWon(game):
        return game.chosenDoors[0] == game.rewardDoor


class FirstDoorNonReward(SuccessDefinition):
    def hasWon(game):
        return game.chosenDoors[0] != game.rewardDoor


AllDefinitions = [RewardDoor, NonRewardDoor,
                  FirstDoorReward, FirstDoorNonReward]

class SuccessDefinition():
    def hasWon(game):
        return False


class RewardDoor(SuccessDefinition):
    def hasWon(game):
        return game.chosenDoor == game.rewardDoor


class NoRewardDoor(SuccessDefinition):
    def hasWon(game):
        return game.chosenDoor != game.rewardDoor


class InitDoorReward(SuccessDefinition):
    def hasWon(game):
        return game.chosenDoors[0] == game.rewardDoor


class InitDoorNoReward(SuccessDefinition):
    def hasWon(game):
        return game.chosenDoors[0] != game.rewardDoor


AllDefinitions = [RewardDoor, NoRewardDoor,
                  InitDoorReward, InitDoorNoReward]

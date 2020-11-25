class RewardDoor():
    def hasWon(game):
        return game.chosenDoor == game.rewardDoor


class NonRewardDoor():
    def hasWon(game):
        return game.chosenDoor != game.rewardDoor


class FirstDoorReward():
    def hasWon(game):
        return game.chosenDoors[0] == game.rewardDoor


class FirstDoorNonReward():
    def hasWon(game):
        return game.chosenDoors[0] != game.rewardDoor


AllDefinitions = [RewardDoor, NonRewardDoor,
                  FirstDoorReward, FirstDoorNonReward]

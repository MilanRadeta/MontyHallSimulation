class SuccessDefinition():
    def hasWon(game):
        return False


class CarDoor(SuccessDefinition):
    def hasWon(game):
        return game.chosenDoor == game.rewardDoor


class GoatDoor(SuccessDefinition):
    def hasWon(game):
        return game.chosenDoor != game.rewardDoor


class InitCarDoor(SuccessDefinition):
    def hasWon(game):
        return game.chosenDoors[0] == game.rewardDoor


class InitGoatDoor(SuccessDefinition):
    def hasWon(game):
        return game.chosenDoors[0] is not None and game.chosenDoors[0] != game.rewardDoor


AllDefinitions = [CarDoor, GoatDoor,
                  InitCarDoor, InitGoatDoor]

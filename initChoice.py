from Config import Config
from SuccessDefinition import AllDefinitions
from Simulator import Simulator
from ChoiceStrategy import CommonStrategies, FirstDoor, Random

config = Config()
config.initChoiceStrategy = [Random, FirstDoor]
config.strategy = CommonStrategies
config.successDefinitions = AllDefinitions
config.totalDoors = [3, 5]
config.totalTries = [10**4]
Simulator(config).run()

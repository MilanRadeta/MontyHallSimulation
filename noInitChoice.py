from Config import Config
from SuccessDefinition import AllDefinitions
from Simulator import Simulator
from ChoiceStrategy import CommonStrategies, NoDoor, Random

config = Config()
config.initChoiceStrategy = [Random, NoDoor]
config.strategy = CommonStrategies
config.successDefinitions = AllDefinitions
config.totalDoors = [3, 5]
config.totalTries = [10**3]
Simulator(config).run()

from Config import Config
from SuccessDefinition import AllDefinitions
from Simulator import Simulator
from ChoiceStrategy import AllStrategies

config = Config()
config.strategy = AllStrategies
config.successDefinitions = AllDefinitions
config.totalDoors = [3, 5, 10]
config.totalTries = [10**(i+1) for i in range(5)]
Simulator(config).run()

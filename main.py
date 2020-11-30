from Config import Config
from SuccessDefinition import AllDefinitions
from Simulator import Simulator
from ChoiceStrategy import CommonStrategies

config = Config()
config.strategy = CommonStrategies
config.successDefinitions = AllDefinitions
config.totalDoors = [3, 5, 10]
config.totalTries = [10**i for i in range(3, 5)]
Simulator(config).run()

from Config import Config
from SuccessDefinition import AllDefinitions
from Simulator import Simulator
from ChoiceStrategy import CommonStrategies, FirstDoor

config = Config()
config.initChoiceStrategy = FirstDoor
config.strategy = CommonStrategies
config.successDefinitions = AllDefinitions
config.totalDoors = [3, 5, 10]
config.totalTries = [10**(i+1) for i in range(4)]
Simulator(config).run()

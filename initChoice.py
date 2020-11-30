from Config import Config
from SuccessDefinition import CommonDefinitions
from Simulator import Simulator
from ChoiceStrategy import CommonStrategies, FirstDoor, NoDoor, Random

config = Config()
config.initChoiceStrategy = [Random, FirstDoor, NoDoor]
config.strategy = CommonStrategies
config.successDefinitions = CommonDefinitions
config.totalDoors = [3, 5]
config.totalTries = [10**4]
Simulator(config).run(prefix='initChoice=%s', prefixParams=(
    'initChoiceStrategy',), outputFile='outputs/initChoice.pdf')

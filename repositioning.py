from Config import Config
from SuccessDefinition import CommonDefinitions
from Simulator import Simulator
from ChoiceStrategy import CommonStrategies, RandomClosed, RandomClosedOrReward

config = Config()
config.positioningStrategy = [RandomClosedOrReward, RandomClosed]
config.strategy = CommonStrategies
config.successDefinitions = CommonDefinitions
config.totalDoors = [3, 5]
config.totalTries = [10**4]
Simulator(config).run(prefix='positioning=%s', prefixParams=(
    'positioningStrategy',), outputFile='outputs/positioningStrategy.pdf')

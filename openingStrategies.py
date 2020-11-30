from Config import Config
from SuccessDefinition import CommonDefinitions
from Simulator import Simulator
from ChoiceStrategy import CommonStrategies, RandomClosed, RandomNonChosenEmptyClosed

config = Config()
config.openingStrategy = [RandomNonChosenEmptyClosed, RandomClosed]
config.strategy = CommonStrategies
config.successDefinitions = CommonDefinitions
config.totalDoors = [3, 5]
config.totalTries = [10**4]
Simulator(config).run(prefix='openStrategy=%s', prefixParams=(
    'openingStrategy',), outputFile='outputs/openingStrategy.pdf')

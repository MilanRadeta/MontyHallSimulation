from Simulator import Simulator
from ChoiceStrategy import AllStrategies

Simulator({
    'strategies': AllStrategies,
    'totalDoors': (3, 5, 10),
    'totalTries': [10**(i+1) for i in range(5)],
}).run()

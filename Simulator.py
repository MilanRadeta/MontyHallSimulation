import pandas
from Doors import Doors


class Simulator(object):
    def __init__(self, config):
        self.strategies = config['strategies']
        self.totalDoors = config['totalDoors']
        self.totalTries = config['totalTries']

    def simulate(totalTries, totalDoors, choiceStrategy, log=False):
        if log:
            print(
                f'Running simulation for totalTries={totalTries}, totalDoors={totalDoors}, choiceStrategy={choiceStrategy}')
        wins = 0
        for i in range(totalTries):
            hasWon = Doors(totalDoors, choiceStrategy).runGame()
            if hasWon:
                wins += 1
        return wins

    def run(self):
        for choiceStrategy in self.strategies:
            data = {}
            for numberOfDoors in self.totalDoors:
                data[numberOfDoors] = {}
                for numOfTries in self.totalTries:
                    wins = Simulator.simulate(numOfTries, numberOfDoors, choiceStrategy)
                    data[numberOfDoors][
                        numOfTries] = f'{round(wins/numOfTries * 100, 2)}%'
            print()
            print(choiceStrategy.__name__)
            print(pandas.DataFrame(data))
            print()

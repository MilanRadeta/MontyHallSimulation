import pandas
from Doors import Doors


class Simulator(object):
    def __init__(self, config):
        self.strategies = config['strategies']
        self.successDefinitions = config['successDefinitions']
        self.totalDoors = config['totalDoors']
        self.totalTries = config['totalTries']

    def simulate(totalTries, totalDoors, choiceStrategy, successDefinitions, log=False):
        if log:
            print(
                f'Running simulation for totalTries={totalTries}, totalDoors={totalDoors}, choiceStrategy={choiceStrategy}, successDefinitions={successDefinitions}')
        wins = {}
        for i in range(totalTries):
            hasWon = Doors(totalDoors, choiceStrategy, successDefinitions).runGame()
            for w in hasWon:
                if w not in wins:
                    wins[w] = 0
                wins[w] += 1 if hasWon[w] else 0
        return wins

    def run(self):
        for numOfTries in self.totalTries:
            for numberOfDoors in self.totalDoors:
                data = {}
                for choiceStrategy in self.strategies:
                    data[choiceStrategy.__name__] = {}
                    wins = Simulator.simulate(numOfTries, numberOfDoors, choiceStrategy, self.successDefinitions)
                    data[choiceStrategy.__name__] = {definition: f'{round(wins[definition]/numOfTries * 100, 2)}%' for definition in wins}
                print()
                print(f'Tries: {numOfTries} | Doors: {numberOfDoors}')
                print(pandas.DataFrame(data))
                print()

from Score import Score
from Config import Config
from DoorsGame import DoorsGame


class Simulator(object):

    def __init__(self, config: Config):
        self.config = config
        self.score = Score(config)
        self.currentConfig = Config()
        self.currentConfig.successDefinitions = self.config.successDefinitions

    def simulate(self):
        print(f'Running simulation for {self.currentConfig}...')
        for i in range(self.currentConfig.totalTries):
            result = DoorsGame(self.currentConfig).runGame()
            self.score.update(result, self.currentConfig)

    def run(self):
        print(f'Running simulator...')
        self.score.reset()
        for totalTries in self.config.totalTries:
            for totalDoors in self.config.totalDoors:
                for strategy in self.config.strategy:
                    self.currentConfig.strategy = strategy
                    self.currentConfig.totalDoors = totalDoors
                    self.currentConfig.totalTries = totalTries

                    self.simulate()
                self.score.printByConfig(self.currentConfig)
        self.score.plotAll()

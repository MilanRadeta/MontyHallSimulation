from Score import Score
from Config import Config
from DoorsGame import DoorsGame


class Simulator(object):

    def __init__(self, config: Config):
        self.config = config
        self.score = Score(config)
        self.currentConfig = Config(config)

    def simulate(self):
        print(f'Running simulation for {self.currentConfig}...')
        for i in range(self.currentConfig.totalTries):
            result = DoorsGame(self.currentConfig).runGame()
            self.score.update(result, self.currentConfig)

    def run(self, prefix='', prefixParams=(), outputFile='outputs/output.pdf'):
        print(f'Running simulator...')
        self.score.reset()
        for config in self.config.getSubconfigs(-2):
            self.currentConfig = Config(config)
            for strategy in config.strategy:
                self.currentConfig.strategy = strategy
                self.simulate()
            self.score.printByConfig(self.currentConfig)
        self.score.plotAll(
            prefix=prefix, prefixParams=prefixParams, outputFile=outputFile)

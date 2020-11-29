from numpy.lib.arraysetops import isin
from ChoiceStrategy import Random, RandomClosed


class Config(object):

    def __init__(self, config=None):
        self.strategy = None
        self.totalDoors = None
        self.totalTries = None

        self.openingStrategy = RandomClosed
        self.initChoiceStrategy = Random
        self.successDefinitions = None

        if (config is not None):
            self.__dict__.update(config.__dict__.items())

    def getPrioritizedProps(self):
        return [self.initChoiceStrategy, self.totalTries,
                self.totalDoors, self.strategy, self.successDefinitions]

    def __str__(self):
        return f'<strategy={self.strategy.__name__}, totalDoors={self.totalDoors}, totalTries={self.totalTries}>'

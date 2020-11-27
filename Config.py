from ChoiceStrategy import Random, RandomClosed

class Config(object):

    def __init__(self, config = None):
        self.strategy = None
        self.totalDoors = None
        self.totalTries = None

        self.openingStrategy = RandomClosed
        self.initChoiceStrategy = Random
        self.successDefinitions = None

        if (config is not None):
            self.openingStrategy = config.openingStrategy
            self.initChoiceStrategy = config.initChoiceStrategy
            self.successDefinitions = config.successDefinitions
        

    def __str__(self):
        return f'<strategy={self.strategy.__name__}, totalDoors={self.totalDoors}, totalTries={self.totalTries}>'

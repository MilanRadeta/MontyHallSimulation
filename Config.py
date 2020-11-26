class Config(object):

    def __init__(self):
        self.strategy = None
        self.totalDoors = None
        self.totalTries = None
        self.successDefinitions = None

    def __str__(self):
        return f'<strategy={self.strategy.__name__}, totalDoors={self.totalDoors}, totalTries={self.totalTries}>'

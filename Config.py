class Config():
    def __init__(self):
        self.strategy = None
        self.totalDoors = None
        self.totalTries = None
        self.successDefinitions = None

    def __str__(self):
        return f'<strategy={self.strategy}, totalDoors={self.totalDoors}, totalTries={self.totalTries}, successDefinitions={self.successDefinitions}>'

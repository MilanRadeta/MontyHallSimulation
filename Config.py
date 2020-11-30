from ChoiceStrategy import Random, RandomClosedOrReward, RandomNonChosenEmptyClosed


class Config(object):

    def __init__(self, config=None):
        self.strategy = None
        self.totalDoors = None
        self.totalTries = None

        self.openingStrategy = RandomNonChosenEmptyClosed
        self.positioningStrategy = RandomClosedOrReward
        self.initChoiceStrategy = Random
        self.successDefinitions = None

        if (config is not None):
            self.__dict__.update(config.__dict__.items())

    def getPrioritizedProps(self):
        return [self.openingStrategy, self.positioningStrategy, self.initChoiceStrategy, self.totalTries,
                self.totalDoors, self.strategy, self.successDefinitions]

    def getPrioritizedPropKeys(self):
        return ["openingStrategy", "positioningStrategy", "initChoiceStrategy", "totalTries", "totalDoors", "strategy", "successDefinitions"]

    def getSubconfigs(self, depth):
        res = [self]
        propKeys = self.getPrioritizedPropKeys()[:depth]

        for key in propKeys:
            newSubs = []
            for sub in res:
                newSubs.extend(sub.getSubconfigsByKey(key))
            if (len(newSubs) > 0):
                res = newSubs

        return res

    def getSubconfigsByKey(self, key):
        value = self.__dict__[key]
        res = []
        if isinstance(value, list):
            for elem in value:
                config = Config(self)
                config.__dict__[key] = elem
                res.append(config)
            return res

        return []

    def __str__(self):
        return f'<strategy={self.strategy.__name__}, totalDoors={self.totalDoors}, totalTries={self.totalTries}>'

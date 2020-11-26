from numpy.core.fromnumeric import mean


class ScoreItem(object):
    def __init__(self):
        self.reset()

    def __add__(self, val):
        self.values.append(val)
        return self

    def reset(self):
        self.values = []

    def mean(self):
        return mean(self.values)

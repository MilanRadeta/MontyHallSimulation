from numpy.core.numeric import correlate
from numpy.lib.function_base import cov
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

    def cov(self, other):
        return cov(self.values, other.values)

    def correlate(self, other):
        return 1 - abs(self.mean() - other.mean())

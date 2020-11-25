import pandas
import matplotlib.pyplot as plt
import seaborn as sns
from ScoreItem import ScoreItem
from Config import Config


class Score(object):
    def __init__(self, config: Config):
        self.config = config
        self.reset()

    def reset(self):
        self.score = {}
        for totalTries in self.config.totalTries:
            scoreForTries = {}
            for totalDoors in self.config.totalDoors:
                scoreForDoors = {}
                for strategy in self.config.strategy:
                    scoreForStrategy = {}
                    for definition in self.config.successDefinitions:
                        scoreForStrategy[definition.__name__] = ScoreItem()
                    scoreForDoors[strategy.__name__] = scoreForStrategy
                scoreForTries[totalDoors] = scoreForDoors
            self.score[totalTries] = scoreForTries

    def incScore(self, config, name, val):
        scores = self.score[config.totalTries][config.totalDoors][config.strategy.__name__]
        scores[name] += val

    def update(self, score, config):
        for definition in score:
            self.incScore(config, definition,
                          1 if score[definition] else 0)

    def processScores(self, scores):
        print('PROBABILITIES')
        data = {}
        for (strategy, definitions) in scores.items():
            data[strategy] = {}
            for (definition, score) in definitions.items():
                data[strategy][definition] = score.mean()
        return data

    def printScores(self, scores, config):
        print()
        print('PROBABILITIES')
        print(f'Tries: {config.totalTries} | Doors: {config.totalDoors}')
        print(scores)
        print()

    def plotScores(self, scores, config):
        sns.heatmap(scores, annot=True)
        plt.xticks(rotation=0)
        plt.text(x=1.75, y=-0.3, s='PROBABILITIES',
                 fontsize=16, weight='bold')
        plt.text(x=1.8, y=-0.2, s=f'sims={config.totalTries}, doors={config.totalDoors}',
                 fontsize=10, weight='normal')
        plt.show()

    def printByConfig(self, config: Config):
        scores = self.score[config.totalTries][config.totalDoors]
        scores = self.processScores(scores)
        scores = pandas.DataFrame(scores)
        self.printScores(scores, config)
        self.plotScores(scores, config)

    def print(self):
        for (totalTries, doors) in self.score.items():
            print()
            for totalDoors in doors:
                config = Config()
                config.totalTries = totalTries
                config.totalDoors = totalDoors
                self.printByConfig(config)
            print()

    def __iter__(self):
        return self.score.__iter__()

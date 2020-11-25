from Config import Config
import pandas


class Score(object):
    def __init__(self, config):
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
                        scoreForStrategy[definition.__name__] = 0
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

    def printSingleScore(self, scores, totalTries):
        print('PROBABILITIES')
        data = {}
        for (strategy, definitions) in scores.items():
            data[strategy] = {}
            for (definition, score) in definitions.items():
                data[strategy][definition] = f'{round(score/totalTries * 100, 2)}%'
        print(pandas.DataFrame(data))

    def printByConfig(self, config):
        scores = self.score[config.totalTries][config.totalDoors]
        print()
        print(f'Tries: {config.totalTries} | Doors: {config.totalDoors}')
        self.printSingleScore(scores, config.totalTries)
        print()

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

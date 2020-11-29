import seaborn as sns
import pandas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from ScoreItem import ScoreItem
from Config import Config

plt.rcParams['xtick.labelsize'] = plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['figure.figsize'] = (16, 16)
plt.rcParams['figure.titlesize'] = 15


class Score(object):
    def __init__(self, config: Config):
        self.config = config
        self.axes = []
        for prop in config.getPrioritizedProps():
            self.axes.append(prop if (isinstance(prop, list)) else [prop])
        self.reset()

    def getKey(self, prop):
        return prop.__name__ if isinstance(
            prop, type) else prop

    def getSubscore(self, config, depth):
        score = self.score
        props = config.getPrioritizedProps()[:depth]
        for prop in props:
            score = score[self.getKey(prop)]
        return score

    def reset(self):
        self.score = {}

        subscores = [self.score]
        i = 0
        for axis in self.axes:
            i += 1
            newSubscores = []
            for score in subscores:
                for elem in axis:
                    key = self.getKey(elem)
                    if i == len(self.axes):
                        score[key] = ScoreItem()
                    else:
                        subscore = {}
                        newSubscores.append(subscore)
                        score[key] = subscore
            subscores = newSubscores

    def incScore(self, config, name, val):
        score = self.getSubscore(config, -1)
        score[name] += val

    def update(self, score, config):
        for definition in score:
            self.incScore(config, definition,
                          1 if score[definition] else 0)

    def processScores(self, scores):
        data = {}
        for (strategy, definitions) in scores.items():
            data[strategy] = {}
            for (definition, score) in definitions.items():
                data[strategy][definition] = score.mean()
        return data

    def printScores(self, scores, config):
        print()
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
        scores = self.getSubscore(config, -2)
        scores = self.processScores(scores)
        scores = pandas.DataFrame(scores)
        self.printScores(scores, config)

    def plotAll(self, outputFile='output.pdf'):
        print(f'Plotting results...')

        subconfigs = self.config.getSubconfigs(-4)

        rows = len(subconfigs) * len(self.config.totalTries)
        cols = len(self.config.totalDoors)

        index = 0
        for config in subconfigs:
            for totalTries in config.totalTries:
                for totalDoors in config.totalDoors:
                    index += 1
                    scores = self.getSubscore(config, -4)
                    scores = scores[totalTries][totalDoors]
                    scores = self.processScores(scores)
                    scores = pandas.DataFrame(scores)

                    ax = plt.subplot(rows, cols, index)
                    ax.set_title(
                        f'initChoice: {config.initChoiceStrategy.__name__} \n sims={totalTries}, doors={totalDoors}')
                    sns.heatmap(scores, ax=ax, annot=True)

        print(f'Saving to {outputFile}...')
        pdf = PdfPages(outputFile)
        pdf.savefig()
        pdf.close()
        print(f'Finished saving.')

    def __iter__(self):
        return self.score.__iter__()

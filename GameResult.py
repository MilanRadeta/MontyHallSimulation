class GameResult(object):
    def __init__(self, game):
        self.definitions = {}
        for definition in game.config.successDefinitions:
            self.definitions[definition.__name__] = definition.hasWon(game)

    def __iter__(self):
        return self.definitions.__iter__()

    def __getitem__(self, name):
        return self.definitions[name]

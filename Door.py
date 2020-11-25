class Door(object):
    def __init__(self, index):
        self.index = index
        self.isOpen = False
        self.hasReward = False
        self.isChosen = False

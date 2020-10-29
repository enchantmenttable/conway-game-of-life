class Cell:
    def __init__(self, state=0, y=0, x=0):
        self.state = state
        self.y = y
        self.x = x


class Universe:
    def __init__(self, w=20, h=20):
        self.width = w
        self.height = h  # width and height will be extended? if not, delete them
        self.surface = [[Cell() for _ in range(w)] for _ in range(h)]

    def neighbor_assessment(self):
        self.surface[y][x]


def initialize():
    pass


def render():
    pass

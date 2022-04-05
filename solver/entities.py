import numpy as np


class Cell:

    up = 0
    right = 0
    down = 0
    left = 0

    def get_info(self):
        return "{} up\n{} right\n{} down\n{} left".format(self.up, self.right, self.down, self.left)

    def __init__(self, up, right, down, left):
        self.up = up
        self.right = right
        self.down = down
        self.left = left


class Maze:

    dim = [0, 0]
    cells = []

    def __init__(self, dim, cells):
        self.dim = dim
        self.cells = cells


class Agent:

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

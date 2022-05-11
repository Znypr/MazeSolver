import numpy as np


class Cell:

    up = 0
    right = 0
    down = 0
    left = 0

    def get_info(self):
        return "{} up\n{} right\n{} down\n{} left".format(self.up, self.right, self.down, self.left)

    def get_walls(self):
        return [self.up, self.right, self.down, self.left]

    def __init__(self, up, right, down, left):
        self.up = up
        self.right = right
        self.down = down
        self.left = left

class Exit:

    position = [0, 0]
    up = 0
    right = 0
    down = 0
    left = 0

    def get_position(self):
        return self.position

    def get_exits(self):
        return [self.up, self.right, self.down, self.left]


    def __init__(self, x, y, exits):
        self.position[0] = x
        self.position[1] = y
        self.up = exits[0]
        self.right = exits[1]
        self.down = exits[2]
        self.left = exits[3]



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

import numpy as np
import random


class Cell:

    up = 0
    right = 0
    down = 0
    left = 0

    def set_weight(self, weight):
        self.weight = weight

    def get_info(self):
        return "{} up\n{} right\n{} down\n{} left".format(self.up, self.right, self.down, self.left)

    def get_walls(self):
        return [self.up, self.right, self.down, self.left]

    def get_position(self):
        return self.position

    def __init__(self, up, right, down, left, x, y):
        self.position = [x, y]
        self.weight = -1
        self.up = up
        self.right = right
        self.down = down
        self.left = left

class Exit:

    def get_position(self):
        return self.position

    def get_exits(self):
        return [self.up, self.right, self.down, self.left]


    def __init__(self, x, y, exits):
        self.position = [0, 0]
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

    rotation = 0 # 0:360
    x = 0
    y = 0

    def __init__(self, x, y, rotation):
        self.x = x
        self.y = y
        self.rotation = rotation

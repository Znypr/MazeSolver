import random
from turtle import position
import numpy as np


class Neural:

    alpha = 0.1
    gamma = 0.9
    epsilon = 0.01

    states = []
    action = [1, 1, -1, -1]
    qt = np.zeros((len(states), len(action)))
    state = 0

    position = []
    maze = None

    # PHYSICS

    def collision(self, x, y):
        cx, cy = self.position[0], self.position[1]

        if (
            x > 0 and self.maze.cells[cx][cy].right == 1 or
            x < 0 and self.maze.cells[cx][cy].left == 1 or
            y < 0 and self.maze.cells[cx][cy].up == 1 or
            y > 0 and self.maze.cells[cx][cy].down == 1
        ):
            return False

        else:
            return True

    def out_of_bounds(self):
        cx, cy = self.position[0], self.position[1]

        if (
            cx > self.maze.dim[0]-1 or cx < 0 or
            cy > self.maze.dim[1]-1 or cy < 0
        ):
            return True

        else:
            return False

    def move_agent(self, x, y):
        if self.collision(x, y):
            self.position[0] += x
            self.position[1] += y
        else:
            print("Illegal Move")

        if self.out_of_bounds():
            print("Out of Bounds")

        print("{},{}".format(self.position[0], self.position[1]))

    def move(self, x=None, y=None, moves=None):
        if moves:
            for i in range(0, len(moves)-1, 2):
                self.move_agent(moves[i], moves[i+1])
        else:
            self.move_agent(x, y)

    # LEARNING

    def get_max(self, arr):
        idx, max = 0, 0
        for i in range(len(arr)):
            if arr[i] > max:
                max = arr[i]
                idx = i
        return max, idx

    def get_environment(self):
        return [self.position[0], self.position[1], self.cells]

    def get_state(self):
        env = self.get_environment()
        s = env[0]
        for i in range(1, len(env)):
            s = s * self.limit[i] + env[i]
        return s

    def select_action(self):
        p = random.random()
        if p > self.epsilon:
            val, idx = self.get_max(self.Q_t[self.state])
            return idx
        else:
            return random.randrange(0, len(self.action))

    def init_q(self):
        for i in range(len(self.qt)):
            for j in range(len(self.qt[0])):
                rand = random.uniform(0.01, 0.001)
                self.Q_t[i][j] = rand

    def update_q(self, new_state, action):
        val, idx = self.get_max(self.Q_t[new_state])
        self.Q_t[self.state][action] = self.Q_t[self.state][action] + \
            self.alpha * (self.reward + self.gamma * val -
                          self.Q_t[self.state][action])

    def __init__(self, maze, agent):
        self.maze = maze
        self.position = [agent.x, agent.y]

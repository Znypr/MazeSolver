import sys
import os
import csv
import math

import controller.control as c
import maze_detection as d
import solver as s


#import visualizer.visualize as v

def convert(path):
    instructions = []
    for move in path:
        if move == 0:
            instructions.append('f')
        elif move == 1:
            instructions.append('r')
        elif move == -1:
            instructions.append('l')
        elif move == 2:
            instructions.append('b')
    return instructions


if __name__ == "__main__":

    # Detection
    # maze, pos = d.detect()

    # Solver
    # actions = s.solve(maze, pos)

    # Visualize
    # v.visualize(maze, pos, actions)

    #maze = nt.Maze(dim, cells)

    # v.visualize(maze)

    # Control
    c.move(p1)

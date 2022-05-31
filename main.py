import sys
import os
import csv

import controller.control as c
import maze_detection as d
import solver as s


#import visualizer.visualize as v


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
    path = ['r', 'r', 'f', 'l', 'l', 'f']

    c.move(path)

#!/usr/bin/env pybricks-micropython

import solver as s
import maze_detection as d
import os
import sys
import csv
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)


#import visualizer.visualize as v


# import ../db.py

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
    actions = ['stop']

    with open('../controller/actions.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(actions)

    0

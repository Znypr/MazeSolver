import maze_detection.detect as d
import controller.control as c
import visualizer.visualize as v
import solver.solve as s
import solver.entities as nt
import sys
import os
import csv
import math

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

    maze = d.detect_lab('media\images\maz3.jpg')
    agent = nt.Agent(2,0)

    v.visualize(maze, agent)

    exits = s.find_exits(maze)

    s.set_lab_weights(maze, exits)

    s.escape_maze(maze, agent)


    # Control
    c.move(p1)

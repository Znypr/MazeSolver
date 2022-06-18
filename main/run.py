import sys
import os
import csv
import math

import detector.detect as d
import controller.control as c
import visualizer.visualize as v
import solver.solve as s
import solver.entities as nt

def main():

    simulate = True

    # Connection
    c.establish_connection() if not simulate else None

    # Detection
    maze = d.detect_maze('input/maz3.jpg', False) # flag for visualizing images
    agent = nt.Agent(2, 0, 180) # x,y,rotation

    # Visualize
    v.visualize(maze, agent)
    exits = s.find_exits(maze)

    # Learn
    s.set_lab_weights(maze, exits)
    s.escape_maze(maze, agent, simulate)

if __name__ == "__main__":

    main()
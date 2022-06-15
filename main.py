import sys
import os
import csv
import math

import maze_detection.detect as d
import controller.control as c
import visualizer.visualize as v
import solver.solve as s
import solver.entities as nt


if __name__ == "__main__":

    # Connection
    #c.establish_connection()

    # Detection
    maze = d.detect_maze('media\images\maz3.jpg', False)
    agent = nt.Agent(2, 0, 180) # x,y,rotation

    # Visualize
    #v.visualize(maze, agent)
    exits = s.find_exits(maze)

    # Learn
    s.set_lab_weights(maze, exits)
    #s.escape_maze(maze, agent)

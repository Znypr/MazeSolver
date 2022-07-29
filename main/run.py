import sys
import os
import csv
import math
import glob
import argparse

import detector.detect as d
import controller.control as c
import visualizer.visualize as v
import solver.solve as s
import solver.entities as nt

def main():

    # Parse arguments
    parser = argparse.ArgumentParser(description='Solve a maze')
    parser.add_argument('-c', '--control', help='flag if robot should be controlled', action='store_true', default=False)
    parser.add_argument('-v', '--visualize', help='flag if detection steps should be visualized', action='store_true', default=True)
    args = parser.parse_args()

    # Connection
    c.establish_connection() if args.control else None

    for maze in glob.glob('input/*0.jpg'):

        print('\n     Current Maze to be solved: {}\n\n'.format(maze))

        # Detection
        try:
            maze = d.detect_maze(maze, args.visualize) # flag for visualizing images
        except Exception as e:
            print('\n     Error: {}\n'.format(e))
            continue

        agent = nt.Agent(2, 0, 180) # x,y,rotation

        # Visualize
        v.visualize(maze, agent)
        exits = s.find_exits(maze)

        # Learn
        s.set_lab_weights(maze, exits)
        s.escape_maze(maze, agent, args.control)

        if  input('Do you want to continue? (y/n)') == 'n':
            break
    
    print('\nAll mazes have been solved!')

if __name__ == "__main__":

    main()

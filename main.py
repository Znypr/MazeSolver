import os
import sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
import controller.main as c



import maze_detection as d
#import visualizer.visualize as v
import solver as s
import solver.entities as nt


# import ../db.py

if __name__ == "__main__":

    # Detection
    # maze, pos = d.detect()

    # Solver
    # actions = s.solve(maze, pos)

    # Visualize
    # v.visualize(maze, pos, actions)

    dim = [3, 2]
    cells = [
        [nt.Cell(1, 0, 0, 1),
         nt.Cell(0, 0, 1, 0)],
        [nt.Cell(1, 0, 1, 0),
         nt.Cell(1, 1, 1, 0)],
        [nt.Cell(1, 0, 0, 0),
         nt.Cell(0, 1, 0, 1)]
    ]

    #maze = nt.Maze(dim, cells)

    # v.visualize(maze)

    # Control
    #c.move(['f', 'r', 'f'])

    0

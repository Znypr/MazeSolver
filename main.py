from controller import move
import maze_detection as d
#import visualizer.visualize as v
import solver as s
import solver.entities as nt

import sys
sys.path.append("../controller")

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

    move("f")

    0

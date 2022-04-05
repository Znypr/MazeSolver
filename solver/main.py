import neural as n
import entities as nt
import numpy as np

if __name__ == "__main__":

    dim = [3, 2]
    cells = [
        [nt.Cell(1, 0, 0, 1),
         nt.Cell(0, 0, 1, 0)],
        [nt.Cell(1, 0, 1, 0),
         nt.Cell(1, 1, 1, 0)],
        [nt.Cell(1, 0, 0, 0),
         nt.Cell(0, 1, 0, 1)]
    ]

    maze = nt.Maze(dim, cells)
    agent = nt.Agent(0, 1)

    engine = n.Neural(maze, agent)

    engine.move(0, -1)
    engine.move(moves=[1, 0, 1, 0, 0, 1, -1, 0])

    0

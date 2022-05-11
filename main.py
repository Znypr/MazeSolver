import maze_detection as d
import visualizer.visualize as v
import solver.solve as s
import solver.entities as nt

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

    maze = nt.Maze(dim, cells)
    agent = nt.Agent(1, 1)

    v.visualize(maze, agent)

    agent = nt.Agent(0, 1)
    v.updateAgent(agent)

    agent = nt.Agent(0, 0)
    v.updateAgent(agent)

    agent = nt.Agent(1, 0)
    v.updateAgent(agent)

    agent = nt.Agent(2, 0)
    v.updateAgent(agent)

    agent = nt.Agent(2, 1)
    v.updateAgent(agent)
    
    agent = nt.Agent(2, 2)
    v.updateAgent(agent)

    exits = s.find_exits(maze)
    for exit in exits:
        print(exit.get_position(), exit.get_exits())

    # Control
    # c.move(actions)

    0

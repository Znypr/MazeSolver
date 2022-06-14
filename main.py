import maze_detection.detect as d
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

    maze = d.detect_lab('media\images\maz3.jpg')
    agent = nt.Agent(1, 1)

    v.visualize(maze, agent)

    exits = s.find_exits(maze)

    s.det_q_learn(maze, exits)


    # Control
    # c.move(actions)

    0

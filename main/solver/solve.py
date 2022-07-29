import numpy as np

import solver.entities as nt
import visualizer.visualize as v
import controller.control as c

def find_exits(maze):
    cells = maze.cells
    exit_cells = []

    for i_column, column in enumerate(cells):
        last_column = len(cells)-1
        for i_row, cell in enumerate(column):
            last_row = len(column)-1
            walls = cell.get_walls()
            exit_on_top = i_row == 0 and walls[0] == 0
            exit_on_right = i_column == last_column and walls[1] == 0
            exit_at_bottom = i_row == last_row and walls[2] == 0
            exit_on_left = i_column == 0 and walls[3] == 0
            if(exit_on_top or exit_on_right or exit_at_bottom or exit_on_left):
                exits = [0, 0, 0, 0]
                if(exit_on_top): exits[0] = 1
                if(exit_on_right): exits[1] = 1
                if(exit_at_bottom): exits[2] = 1
                if(exit_on_left): exits[3] = 1
                exit_cells.append(nt.Exit(i_column, i_row, exits))
    
    return exit_cells

def set_lab_weights(maze, exits):
    cells = maze.cells
    current_cells = []
    weight = 1

    dims = maze.dim
    x_maze = dims[0]
    y_maze = dims[1]

    for exit in exits:
        pos = exit.get_position()
        current_cells.append(cells[pos[0]][pos[1]])

    changed = True

    while(changed):
        changed = False
        new_cells = []
        for cell in current_cells:
            cell.set_weight(weight)
            pos = cell.get_position()
            x = pos[0]
            y = pos[1]

            for i, pos in enumerate([(x-1,y),(x,y-1),(x+1,y),(x,y+1)]):
                if(0 <= pos[0] < x_maze and 0 <= pos[1] < y_maze):
                    if(cell.left == False and i == 0 or cell.up == False and i == 1 or cell.right == False and i == 2 or cell.down == False and i == 3):
                        new_cell = cells[pos[0]][pos[1]]
                        if(new_cell.weight < 0):
                            new_cells.append(new_cell)
                            changed = True

        current_cells = new_cells
        weight += 1
        v.color_cells(maze)
    
def calculate_move(agent, i):

    move = []
    d_rot = (i*90 - agent.rotation + 360) % 360

    if(d_rot == 0): # straight
        move = [0]
    elif(d_rot == 90): # turn right
        move = [1, 0]
    elif(d_rot == 180): # turn right twice
        move = [1, 1, 0]
    elif(d_rot == 270): # turn left
        move = [-1, 0]

    agent.rotation = (agent.rotation + d_rot) % 360

    return move

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

def escape_maze(maze, agent, control):

    cells = maze.cells

    dims = maze.dim
    x_maze = dims[0]
    y_maze = dims[1]

    x = agent.x
    y = agent.y
    agent_cell = cells[x][y]
    agent_weight = agent_cell.weight

    while(agent_weight > 1):
        for i, pos in enumerate([(x,y-1),(x+1,y),(x,y+1),(x-1,y)]):
            if(0 <= pos[0] < x_maze and 0 <= pos[1] < y_maze): # out of bounds check
                if(agent_cell.up == False and i == 0 or agent_cell.right == False and i == 1 or agent_cell.down == False and i == 2 or agent_cell.left == False and i == 3): # legal move
                    new_cell = cells[pos[0]][pos[1]]
                    if(new_cell.weight < agent_weight):
                        agent_cell = new_cell
                        break
            

        agent_pos =  agent_cell.get_position()
        x = agent_pos[0]
        y = agent_pos[1]
        agent.x = x
        agent.y = y
        v.updateAgent(agent)
        agent_weight = agent_cell.weight

        instructions = calculate_move(agent, i)
        print(convert(instructions))
        c.move(convert(instructions)) if control else None
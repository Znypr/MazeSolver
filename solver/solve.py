import solver.entities as nt
import visualizer.visualize as v
import numpy as np

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

def det_q_learn(maze, exits):
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
    
        
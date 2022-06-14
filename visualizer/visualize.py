import PySimpleGUI as sg
import numpy as np

wallWidth = 12
cellDims = 200
wallLength = cellDims - 2 * wallWidth
margin = 40
playerDims = cellDims/4

def visualize(maze, agent):

    global lastAgentX
    global lastAgentY
    global playerRef
    global window

    lastAgentX = agent.x
    lastAgentY = agent.y

    cells = maze.cells
    dim = maze.dim
    dimX = dim[0]
    dimY = dim[1]

    canvas = sg.Graph((dimX * (wallLength + wallWidth) + (2*margin + wallWidth), dimY * (wallLength + wallWidth) + (2 * margin + wallWidth)), (-margin, dimY * (wallLength + wallWidth) + margin + wallWidth), (dimX * (wallLength + wallWidth) + margin + wallWidth, -margin), background_color = "white", k="GRAPH")
    
    window = sg.Window(title="Maze", layout=[[canvas]], finalize = True, margins=(50, 50))

    for x in range(dimX + 1):
        for y in range(dimY + 2):
            topLeft = (x * (wallLength + wallWidth), y * (wallLength + wallWidth))
            bottomRight = (topLeft[0] + wallWidth, topLeft[1] + wallWidth)
            window["GRAPH"].draw_rectangle(topLeft, bottomRight, fill_color = "darkgrey", line_color = "darkgrey", line_width = 0)

    for columnId, column in enumerate(cells):
        for rowId, cell in enumerate(column):
            walls = cell.get_walls()
            for wall_id, wall in enumerate(walls):
                if(wall):
                    startPoint = (columnId * (wallLength + wallWidth) + (wall_id == 1) * (wallLength + wallWidth) + (wall_id % 2 == 1) * wallWidth / 2 + (wall_id % 2 == 0) * wallWidth, rowId * (wallLength + wallWidth) + (wall_id == 2) * (wallLength + wallWidth) + (wall_id % 2 == 1) * wallWidth + (wall_id % 2 == 0) * wallWidth / 2)
                    endPoint = (startPoint[0] + (wall_id % 2 == 0) * wallLength, startPoint[1] + (wall_id % 2 == 1) * wallLength)
                    window["GRAPH"].draw_line(startPoint, endPoint, color="black", width=wallWidth)
    
    agentPoint = (agent.x * (wallLength + wallWidth) + cellDims / 2, agent.y * (wallLength + wallWidth) + cellDims / 2)
    
    playerRef = window["GRAPH"].draw_point( agentPoint, size=playerDims, color="black")

    window.read(1000)

def updateAgent(agent):
    global playerRef
    global lastAgentX
    global lastAgentY
    global window

    startPoint = (lastAgentX * (wallLength + wallWidth) + cellDims / 2 , lastAgentY * (wallLength + wallWidth) + cellDims / 2)
    agentPoint = (agent.x * (wallLength + wallWidth) + cellDims / 2, agent.y * (wallLength + wallWidth) + cellDims / 2)
    window["GRAPH"].draw_line(startPoint, agentPoint, color="black", width=playerDims/4)
    window["GRAPH"].delete_figure(playerRef)

    lastAgentX = agent.x
    lastAgentY = agent.y
    playerRef = window["GRAPH"].draw_point( agentPoint, size=playerDims, color="black")
    window.read(1000)

def color_cells(maze):
    global window
    global playerRef

    cells = maze.cells
    dims = maze.dim
    weights = np.zeros(dims)
    for ir, row in enumerate(cells):
        row_weights = [cell.weight for cell in row]
        weights[ir] = row_weights

    max_weight = np.amax(weights)

    for i_row, row in enumerate(cells):
        for i_cell, cell in enumerate(row):
            cell_weight = cell.weight
            if(cell_weight >= 0):
                color = (2.0 * cell_weight/max_weight, 2.0 * ( 1 - cell_weight/max_weight), 0)
            else:
                color = (1, 1, 1)

            cell_middle_point = (i_row * (wallLength + wallWidth) + cellDims/2, i_cell * (wallLength + wallWidth) + cellDims/2)

            top_left = (cell_middle_point[0] - wallLength/2, cell_middle_point[1] - wallLength/2)
            bottom_right = (cell_middle_point[0] + wallLength/2, cell_middle_point[1] + wallLength/2)

            color = to_hex(color[0], color[1], color[2])
            cell = window["GRAPH"].draw_rectangle(top_left, bottom_right, fill_color = color, line_width = 0)

    window["GRAPH"].bring_figure_to_front(playerRef)
    window.read(1000)

def to_hex(r, g, b):
    values = np.array([r,g,b])
    values *= 255
    values = np.clip(values, 0, 255)
    hex =  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    output =  '#'
    for value in values:
        output += hex[int(value/16)] + hex[int(value%16)]
    return output




        
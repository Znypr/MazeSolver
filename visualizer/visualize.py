import PySimpleGUI as sg

def visualize(maze):
    cells = maze.cells
    dim = maze.dim
    dimX = dim[0]
    dimY = dim[1]

    canvas = sg.Graph((dimX * 100 + 40, dimY * 100 + 40), (-20, dimY * 100 + 20), (dimX * 100 + 20, -20), background_color = "white", k="GRAPH")

    window = sg.Window(title="Maze", layout=[[canvas]], finalize = True, margins=(50, 50))

    window["GRAPH"].draw_line((0,0), (0,100), color="black", width=5)

    window.read()
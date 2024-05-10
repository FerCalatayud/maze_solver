# Internal
from maze_solver.graphics import Window
from maze_solver.maze import Maze

def main():

    win = Window(800, 600)
    
    main_maze = Maze(0, 0, 12, 10, 10, 10, win)
    main_maze._create_cells()

    win.wait_for_close()

main()
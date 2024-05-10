# Internal
from maze_solver.graphics import Window
from maze_solver.maze import Maze

def main():

    win = Window(800, 600)
    
    main_maze = Maze(100, 100, 5, 5, 10, 10, win)

    win.wait_for_close()

main()
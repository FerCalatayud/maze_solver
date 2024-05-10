# Internal
from maze_solver.graphics import Window
from maze_solver.maze import Maze

def main():

    win = Window(800, 600)
    
    main_maze = Maze(100, 50, 10, 10, 50, 50, win, seed=1)

    main_maze.solve()

    win.wait_for_close()

main()
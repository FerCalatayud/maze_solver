# Python
from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("My Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="gray", height=height, width=width)
        self.__canvas.pack()
        self.__window_running = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__window_running = True
        while self.__window_running:
            self.redraw()

    def close(self):
        self.__window_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color=fill_color)

class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Line():
    def __init__(self, point_1, point_2) -> None:
        self.__point_1 = point_1
        self.__point_2 = point_2
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
                        self.__point_1.x, self.__point_1.y, 
                        self.__point_2.x, self.__point_2.y, 
                        fill=fill_color, width=2
                    )

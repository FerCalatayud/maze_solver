# Internal
from maze_solver.graphics import Point, Line

class Cell():
    def __init__(self, window = None) -> None:
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.__x_top_left =  None
        self.__y_top_left =  None
        self.__x_bottom_right =  None
        self.__y_bottom_right =  None
        self.__window = window
        self.visited = False
    
    def draw(self, x_top_left, y_top_left, x_bottom_right, y_bottom_right):

        self.__x_top_left =  x_top_left
        self.__y_top_left =  y_top_left
        self.__x_bottom_right =  x_bottom_right
        self.__y_bottom_right =  y_bottom_right

        # zero coordinates are top left
        # always draw following the coordinates in ascending, for example from 0 to n
        # point_a is the top left point, then point_b to the right the top right. Finally point_c is bottom left and point_d bottom right
        point_a = Point(self.__x_top_left, self.__y_top_left)
        point_d = Point(self.__x_bottom_right, self.__y_bottom_right)
        point_b = Point(self.__x_bottom_right, self.__y_top_left)
        point_c = Point(self.__x_top_left, self.__y_bottom_right)

        if self.left_wall:
            self.__window.draw_line(Line(point_c, point_a), "black")
        else:
            self.__window.draw_line(Line(point_c, point_a), "gray")

        if self.right_wall:
            self.__window.draw_line(Line(point_d, point_b), "black")
        else:
            self.__window.draw_line(Line(point_d, point_b), "gray")

        if self.top_wall:
            self.__window.draw_line(Line(point_a, point_b), "black")
        else:
            self.__window.draw_line(Line(point_a, point_b), "gray")

        if self.bottom_wall:
            self.__window.draw_line(Line(point_c, point_d), "black")
        else:
            self.__window.draw_line(Line(point_c, point_d), "gray")

    def draw_move(self, to_cell, undo=False):
        # calculates the two central points of the cells
        # specifically calculates the half of the size of each x and y lines, and finally adds it to the top left point coordinates
        start_cell_central_point_x = (abs(self.__x_bottom_right - self.__x_top_left) // 2) + self.__x_top_left
        start_cell_central_point_y = (abs(self.__y_bottom_right - self.__y_top_left) // 2) + self.__y_top_left
        end_cell_starting_point_x = (abs(to_cell.__x_bottom_right - to_cell.__x_top_left) // 2) + to_cell.__x_top_left
        end_cell_starting_point_y = (abs(to_cell.__y_bottom_right - to_cell.__y_top_left) / 2) + to_cell.__y_top_left

        starting_point = Point(start_cell_central_point_x, start_cell_central_point_y)
        ending_point = Point(end_cell_starting_point_x, end_cell_starting_point_y)

        if undo:
            self.__window.draw_line(Line(starting_point, ending_point), fill_color="red")
        else:
            self.__window.draw_line(Line(starting_point, ending_point), fill_color="green")

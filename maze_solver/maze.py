# Internal
from maze_solver.cell import Cell

# Python
import time

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
    ) -> None:

        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        # Create cells base on the number of rows and columns
        print(f"=============\n Creating the cells \n=============")
        self.cells = []
        for col in range(1 , self.num_cols + 1):
            #print(f"Appending to Column: {col}")
            column = []
            for row in range(1, self.num_rows + 1):
                #print(f"Appending to Row: {row}")
                column.append(Cell(self.__win))
            
            self.cells.append(column)

        print(f"=============\n Now we go to Drawing the cells \n=============")

        for column_indx in range(0, len(self.cells)):
            # Each cell that here is within a column is in fact in a row 
            # because each slot in a column represents a row
            for row_indx in range(0, len(column)):
                #print(f"Drawing a cell in column: {column_indx}, and row: {row_indx}")
                self._draw_cell(column_indx, row_indx)
    
    def _draw_cell(self, column_indx, row_indx):
        if self.__win is None:
            return

        current_cell = self.cells[column_indx][row_indx]

        # This calculates the left x coordinate of each cell
        x_top_left = self.x1 + (column_indx * self.cell_size_x)
        # This calculates the top y coordinate of each cell
        y_top_left = self.y1 + (row_indx * self.cell_size_y)

        x_bottom_right = x_top_left + self.cell_size_x
        y_bottom_right = y_top_left + self.cell_size_y

        #print(f"Drawing Cell with Point_a: ({x_top_left},{y_top_left}) and Point_d: ({x_bottom_right},{y_bottom_right})")

        current_cell.draw(x_top_left, 
                          y_top_left, 
                          x_bottom_right, 
                          y_bottom_right)

        self._animate()

    def _animate(self):
        if self.__win is None:
            return
        
        self.__win.redraw()
        time.sleep(0.05)
        
    def _break_entrance_and_exit(self):
        self.cells[0][0].top_wall = False
        self._draw_cell(0, 0)

        self.cells[self.num_cols - 1][self.num_rows - 1].bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
